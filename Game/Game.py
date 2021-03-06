from classes.Base import Base
from Game.Rectangle import Rectangle
from Game.Computer import Computer
from Game.Mouse import Mouse
from Game.Image import Image
from Game.Bug import Bug
from Game.Font import Font
from Game.HealthBar import HealthBar
from Game.Text import Text
from Game.Sound import Sound
from Game.Button import Button
from Game.Heal import Heal
import os
import random
import pygame
import math


class Game(Base):
    def __init__(self, aspect_ratio: list = [16, 9], default_size: list = [1024, 576], window_name: str = "game",
                 fps: int = 60):
        # Super
        super().__init__(aspect_ratio, default_size, window_name, fps)

        # Class variables
        self.running = False
        self.passed_seconds = 0
        self.bugs = []
        self.score = 0
        self.__is_game_over = False
        self.is_main_menu = True
        self.color = [255,255,255]
        self.current_color = self.color
        self.next_color = [random.randint(100,255),random.randint(100,255),random.randint(100,255)]
        self.change_background_time = 3
        self.__number_of_steps = 1
        self.step = 1
        self.steps = 1
        self.heals = []

    # running value
    @property
    def running(self) -> bool:
        return self.__running

    @running.setter
    def running(self, value: bool):
        self.__running = value

    # Bugs value
    @property
    def bugs(self) -> list:
        return self.__bugs

    @bugs.setter
    def bugs(self, value: list):
        self.__bugs = value

    def a_second_passed(self):
        self.passed_seconds += 1

        for heal in self.heals:
            if heal.created_at + heal.active_time < self.passed_seconds:
                self.heals.remove(heal)

        is_hit = False
        for bug in self.bugs:
            if self.computer.rect.colliderect(bug.rect):
                is_hit = True
                self.computer.damage(bug.damage)
                
        if is_hit:
            self.sounds["hurt"].play(0)
            
        if self.computer.health <= 0:
            self.is_game_over = True
            
        # making game harder by the time
        if self.passed_seconds > 180:
            for i in range(4):
                self.make_bug()
        elif self.passed_seconds > 90:
            for i in range(2):
                self.make_bug()
        else:
            self.make_bug()
        
        if random.randint(1, 10) == 1:
            self.make_heal()
            
    def make_heal(self):
        x = random.choice(
            [[0, self.computer.x], [self.computer.x+self.computer.width, self.size[0]]])
        x = random.randint(*x)

        y = random.choice(
            [[0, self.computer.y], [self.computer.y+self.computer.height, self.size[1]]])
        y = random.randint(*y)
        
        self.heals.append(Heal(self.heart_image,self.passed_seconds, random.randint(4, 8), random.randint(3, 5), x, y, self.heart_image.width, self.heart_image.height))
    
    @property
    def is_game_over(self) -> bool:
        return self.__is_game_over
    
    @is_game_over.setter
    def is_game_over(self, value: bool):
        self.__is_game_over = value
        if value:
            self.bugs = []
            self.heals = []
            self.computer.health = 100
            self.score_game_over_text.message = f"Score: {self.score}"
            
    def game_over(self):
        """
        Game over statement
        """
        self.screen.fill(self.current_color)

        self.game_over_text.draw(self.screen)
        self.button.draw(self.screen, self.mouse_pointer, self.events)
        self.score_game_over_text.draw(self.screen)

        self.tick()

    def main_menu(self):
        """Main Menu"""

        self.screen.fill(self.current_color)

        self.bugs_text.draw(self.screen)
        self.start_button.draw(self.screen, self.mouse_pointer, self.events)

        for bug in self.demo_bugs:
            bug.draw(self.screen)

        self.tick()

    def make_bug(self) -> Bug:

        x = random.choice(
            [[0, self.computer.x], [self.computer.x+self.computer.width, self.size[0]]])
        x = random.randint(*x)

        y = random.choice(
            [[0, self.computer.y], [self.computer.y+self.computer.height, self.size[1]]])
        y = random.randint(*y)
        
        obstacles = random.randint(1, 5)
        bug = Bug(x, y, obstacles, random.randrange(
            20, 40), random.randrange(20, 40), 6 - obstacles, random.randint(30, 50))
        self.bugs.append(bug)
        
        return bug

    def initiate(self) -> None:
        super(Game, self).initiate()
        self.font = Font(os.path.join("fonts", "yoster.ttf"), 30)
        
        # Sounds
        self.sounds = {
            "shoot": Sound("sounds/hit.wav"),
            "hurt": Sound("sounds/hurt.wav"),
            "main_menu": Sound("musics/menu.mp3"),
            "game": Sound("musics/game.mp3"),
            "coin": Sound("sounds/coin.wav")
        }
        # Heal image
        self.heart_image = Image.load("artworks/heart.png", "heart", 40, 35)
        # Mouse
        self.mouse_pointer = Mouse(0,0, 30, 30, 7)

        # Health bar
        self.health_bar = HealthBar(
            self.font, 0, 20, 200, 50, text_color=self.current_color)
        self.health_bar.x = self.size[0] / 2 - self.health_bar.width / 2
        self.health_bar.calculate_text()

        # Computer
        self.computer = Computer(Image.load(
            "artworks/computer.png", "computer"), 0, 0, 100, 100)
        self.computer.x = self.size[0] / 2 - self.computer.width / 2
        self.computer.y = self.size[1] / 2 - self.computer.height / 2

        font = self.font
        font.size = 60

        # "Game over" text
        self.game_over_text = Text(
            "Game over", self.size[0] / 2, self.size[1] / 2, self.font, center=True)
        self.game_over_text.x -= 20
        self.game_over_text.y -= 200

        # "Bugs" text

        font.size = 120
        self.bugs_text = Text(
            "Bugs", self.size[0] / 2, self.size[1] / 2, self.font, center=True)
        self.bugs_text.x -= 50
        self.bugs_text.y -= 100

        # "Demo bugs"
        self.demo_bugs = [
            Bug(self.bugs_text.x - 30, self.bugs_text.y - 30, 5, 60, 60, 0, 0),
            Bug(self.bugs_text.x + self.bugs_text.width - 170,
                self.bugs_text.y + self.bugs_text.height - 40, 3, 50, 50, 0, 0),
        ]

        font.size = 40

        # "Start" text
        self.start_text = Text("Start", 0, 0, font, self.current_color)

        # Start Button
        self.start_button = Button(
            self.start_text, self.size[0] / 2, self.size[1] / 2 + 100, 300, 80, [0, 0, 255])
        self.start_button.center()
        self.start_button.text.x -= 15

        # "Restart" text
        self.restart_text = Text("Restart", 0, 0, font, self.current_color)

        # "Score" Game over text
        self.score_game_over_text = Text("Score: ", self.size[0] / 2, self.size[1] / 2, font, center=True)
        # Restart button
        self.button = Button(
            self.restart_text, self.size[0] / 2, self.size[1] / 2 + 150, 300, 80, [0, 0, 255])
        self.button.center()
        self.button.text.x -= 15
        
        # Score text
        font.size = 30
        self.score_text = Text(f"Score: {self.score}", 20, 20, font)

        def restart_click():
            self.reset()
            
        def start_click():
            self.reset()

        self.start_button.click = start_click
        self.button.click = restart_click
        

    def reset(self):
        """Resets the game"""
        self.is_game_over = False
        self.is_main_menu = False
        self.running = True
        self.passed_seconds = 0
        self.score = 0
        self.score_text.message = f"Score: {self.score}"
        self.computer.reset()
        self.bugs = []
        self.heals = []
        self.sounds["main_menu"].stop()
        self.sounds["game"].stop()
        self.sounds["game"].play(-1)

    @property
    def number_of_steps(self):
        return self.__number_of_steps
    
    @number_of_steps.setter
    def number_of_steps(self, value):
        self.__number_of_steps = (self.number_of_steps * self.steps + value) / (self.steps + 1)
        self.steps += 1

    def color_transition(self):
        self.number_of_steps = self.change_background_time * self.fps
        self.step += 1
        if self.step < self.number_of_steps:
            self.current_color = [x + (((y-x)/self.number_of_steps)*self.step) for x, y in zip(pygame.color.Color(self.color[0], self.color[1], self.color[2]), pygame.color.Color(self.next_color[0], self.next_color[1], self.next_color[2]))]
        else:
            self.step = 1
            self.color = self.next_color
            self.next_color = [random.randint(100, 255),random.randint(100, 255),random.randint(100, 255)]
            
    def run(self):
        """
        Game loop function
        """
        self.sounds["main_menu"].play(-1)
        self.running = True
        while self.running:
            self.color_transition()
            mouse_coords = pygame.mouse.get_pos()
            self.mouse_pointer.x = mouse_coords[0]
            self.mouse_pointer.y = mouse_coords[1]
            collided_with_mouse = False

            if self.computer.rect.collidepoint(mouse_coords):
                self.mouse_pointer.color = [255, 0, 0]
                collided_with_mouse = True
            else:
                self.mouse_pointer.color = [0, 0, 0]

            # check if pygame wanna quit
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    for bug in self.bugs:
                        # Collide with mouse
                        if not collided_with_mouse and bug.rect.collidepoint(mouse_coords):
                            self.score += bug.damage
                            self.score_text.message = f"Score: {self.score}"
                            self.sounds["shoot"].play(0)
                            self.bugs.remove(bug)
                            break
                    for heal in self.heals:
                        if heal.rect.collidepoint(mouse_coords):
                            self.computer.health += heal.heal_amount
                            self.heals.remove(heal)
                            self.sounds["coin"].play(0)
                            break

            # if it is game over, then do game over statement
            if self.is_game_over:
                self.game_over()
                continue

            if self.is_main_menu:
                self.main_menu()
                continue

            # screen
            self.screen.fill(self.current_color)

            for bug in self.bugs:

                bug.move_to_computer(
                    self.computer, self.calculate_move(bug.speed))
                if bug.mouse_collide(mouse_coords):
                    self.mouse_pointer.color = [0, 255, 0]

                bug.draw(self.screen)
                
            for heal in self.heals:
                heal.draw(self.screen)

            self.health_bar.fill_percentage = self.computer.health

            self.computer.draw(self.screen)
            self.health_bar.draw(self.screen)
            self.score_text.draw(self.screen)
            self.mouse_pointer.draw(self.screen)
            
            # frame rate tick
            self.tick()

from Game.Computer import Computer
from Game.Object import Object
import random
import math
import pygame

class Bug(Object):

    def __init__(self, x: float = 0, y: float = 0, obstacle_count: int = 5, width: int = 20, height: int = 20, damage: int = 0.5, speed: int = 30):
        # Super
        super().__init__(x, y, width, height)

        # Class variables
        self.obstacle_count = obstacle_count
        self.damage = damage
        self.speed = speed
        
    # Obstacle Count property
    @property
    def obstacle_count(self) -> int:
        return self.__obstacle_count
    
    @obstacle_count.setter
    def obstacle_count(self, value: int):
        self.__obstacle_count = value
    
    # Damage property
    @property
    def damage(self) -> int:
        return self.__damage
    
    @damage.setter
    def damage(self, value: int):
        self.__damage = value
        
    # Speed property
    @property
    def speed(self) -> int:
        return self.__speed
    
    @speed.setter
    def speed(self, value: int):
        self.__speed = value
    
    def move_to_computer(self, computer: Computer, speed: float):
        """
        A method for moving towards the computer coords
        """
        # Collide with computer
        if not computer.rect.colliderect(self.rect):
            angle_radians = (math.atan2(self.y - computer.y , self.x - computer.x))
            self.y += -math.sin(angle_radians) * speed
            self.x += -math.cos(angle_radians) * speed
    
    def mouse_collide(self, mouse_coords: list):
        """
        Checking if is it collided with mouse or not
        """
        if self.rect.collidepoint(mouse_coords):
            return True
        return False

    def draw(self, screen):
        """
        A method for drawing the bug
        """
        for i in range(self.obstacle_count):
            
            # Obstacle width and height
            width = self.width / self.obstacle_count - 1
            height = self.height / self.obstacle_count - 1

            x = random.randrange(int(self.x), int(self.x + self.width - width))
            y = random.randrange(int(self.y), int(self.y + self.height - height))

            pygame.draw.rect(screen, [random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)], pygame.Rect(x, y, width, height))
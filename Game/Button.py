from Game.Rectangle import Rectangle
from Game.Text import Text
from Game.Circle import Circle
import pygame

class Button(Rectangle):
    
    def __init__(self, text: Text, x: float=0, y: float=0, width: float=100, height: float=100, color: list=[0, 0, 0]):
        super().__init__(x, y, width, height, color)
        
        self.text = text
        self.hover_sound = pygame.mixer.Sound("sounds/hover.wav")
        self.click_sound = pygame.mixer.Sound("sounds/click.wav")
        self.is_in = False
        
    def center(self):
        super(Button, self).center()
        
        self.text.x = self.x + self.width / 2
        self.text.y = self.y + self.height / 2
        self.text.center_text()
        
    
    def draw(self, screen: pygame.Surface, mouse_pointer: Circle = None, events = None):
        
        if mouse_pointer and events:
            for event in events:
                if self.rect.collidepoint(mouse_pointer.x, mouse_pointer.y):
                    if not self.is_in:
                        self.is_in = True
                        self.hover_sound.play()
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.click_sound.play()
                        self.click()
                else:
                    self.is_in = False
        
        super(Button, self).draw(screen)
        self.text.draw(screen)
        
    def click(self):
        """A function that runs every time that button is clicked"""
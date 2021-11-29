import pygame
from Game.Image import Image
from Game.Object import Object


class Heal(Object):

    def __init__(self, image: Image, created_at: int, heal_amount: int = 5, active_time: int = 5, x: float = 0, y: float = 0, width: float = 0, height: float = 0):
        super().__init__(x, y, width, height)

        self.image = image
        self.heal_amount = heal_amount
        self.active_time = active_time
        self.created_at = created_at
    
    def draw(self, screen: pygame.Surface):
        self.image.x = self.x
        self.image.y = self.y
        self.image.draw(screen)
    

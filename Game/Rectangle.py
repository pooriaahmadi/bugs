import pygame
from Game.Object import Object


class Rectangle(Object):

    def __init__(self, x: float = 0, y: float = 0, width: float = 100, height: float = 100, color: list = [0, 0, 0]):
        super().__init__(x, y, width, height)
        self.color = color

    # Color property
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value: list):
        self.__color = value
        
    def center(self):
        """For centering the box"""
        self.x -= self.width / 2
        self.y -= self.height / 2

    def draw(self, screen: pygame.Surface):
        """
        Draws the rectangle
        :param screen:
        """
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
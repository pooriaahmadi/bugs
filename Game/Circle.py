import pygame
from .Object import Object


class Circle(Object):

    def __init__(self, x: float = 0, y: float = 0, radius: float = 10, color: list = [0, 0, 0]):
        super().__init__(x, y, 0, 0)
        self.radius = radius
        self.color = color

    # Color property
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value: list):
        self.__color = value

    # Radius property
    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, value: float):
        self.__radius = value

    def draw(self, screen: pygame.Surface):
        """
        Draws the circle
        :param screen:
        """
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.radius)

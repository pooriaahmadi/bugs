from __future__ import annotations
from .Object import Object
import pygame


class Image(Object):
    def __init__(self, name: str, image: pygame.image, width: int = None, height: int = None, x: float = 0,
                 y: float = 0):
        super().__init__(x, y, width, height)
        self.name = name
        self.image = image.convert_alpha()
        if self.width and self.height:
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

    # Name property
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    # Image property
    @property
    def image(self) -> pygame.image:
        return self.__image

    @image.setter
    def image(self, value: pygame.image):
        self.__image = value

    def resize(self, width: int, height: int) -> None:
        """
        For resizing the picture with updating the class values
        :param width:
        :param height:
        """
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, screen: pygame.Surface) -> None:
        """
        draws the image on the screen
        """
        screen.blit(self.image, (self.x, self.y))

    @staticmethod
    def load(file_path: str, name: str, width: int = None, height: int = None, x: float = 0, y: float = 0) -> Image:
        """
        Creates a new class from given data
        :param file_path:
        :param name:
        :param x:
        :param y:
        :param width:
        :param height:
        :returns Image:
        """
        return Image(name, pygame.image.load(file_path), width, height, x, y)

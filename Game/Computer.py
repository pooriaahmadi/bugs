import pygame
from .Image import Image
from .Object import Object


class Computer(Object):

    def __init__(self, image: Image, x: float = 0, y: float = 0, width: float = 100, height: float = 100,
                 color: list = [0, 0, 0], health: int = 100):
        super().__init__(x, y, width, height)
        self.color = color
        self.health = health
        self.image = image
        self.image.resize(self.width, self.height)

    # Color property
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value: list):
        self.__color = value

    # Health property
    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, value: int):
        if value > 100:
            self.__health = 100
        else:
            self.__health = value

    # Image property
    @property
    def image(self) -> Image:
        return self.__image

    @image.setter
    def image(self, value: Image):
        self.__image = value
        
    @property
    def rect(self) -> pygame.Rect: 
        """ :returns pygame Rect object: """ 
        
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def reset(self):
        self.health = 100

    def damage(self, amount: int):
        """
        For applying damage
        :param amount:
        """
        self.health -= amount

    def draw(self, screen: pygame.Surface):
        """
        Draws the rectangle
        :param screen:
        """
        self.image.x = self.x
        self.image.y = self.y
        self.image.draw(screen)

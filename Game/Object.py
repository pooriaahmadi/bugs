import pygame

class Object:
    """
    Object class for every object in the game
    """

    def __init__(self, x: float = 0, y: float = 0, width: float = 0, height: float = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # X axis property
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value: float):
        self.__x = value

    # Y axis property
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value: float):
        self.__y = value

    # Width property
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value: float):
        self.__width = value

    # Height property
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value: float):
        self.__height = value

    def list_coordinates(self):
        """
        :returns array of coordinates
        """
        return [self.x, self.y]

    def dict_coordinates(self):
        """
        :returns Dictionary of coordinates
        """
        return {"x": self.x, "y": self.y}

    @property
    def rect(self) -> pygame.Rect:
        """
        :returns pygame Rect object:
        """
        return pygame.Rect(self.x, self.y, self.width, self.height)

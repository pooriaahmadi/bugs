import pygame  # Importing pygame module for game
from pygame.locals import *  # Importing locals for making code more understandable
from Game.Image import Image


class Base:
    """
    Base class for pygame and making things much more easier, this class will be used as a parent
    for customizing the game
    """

    def __init__(self, aspect_ratio: list = [16, 9], size: list = [1024, 576], window_name: str = "game",
                 fps: int = 60):
        self.aspect_ratio = aspect_ratio
        self.size = size
        self.window_name = window_name
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.screen = None
        self.__images = []
        self.current_fps = 0

    # aspect ratio property
    @property
    def aspect_ratio(self):
        return self.__aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, value: list):
        self.__aspect_ratio = value

    # default size property
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value: list):
        self.__size = value

    # window name property
    @property
    def window_name(self):
        return self.__window_name

    @window_name.setter
    def window_name(self, value: str):
        self.__window_name = value

    # fps property
    @property
    def fps(self):
        return self.__fps

    @fps.setter
    def fps(self, value: int):
        self.__fps = value

    # screen property
    @property
    def screen(self):
        return self.__screen

    @screen.setter
    def screen(self, value):
        self.__screen = value

    def initiate(self) -> None:
        """
        initiate function for initiate things in class
        """
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        # setting window name
        pygame.display.set_caption(self.window_name)

        # assigning screen with width and height
        self.screen: pygame.Surface = pygame.display.set_mode(self.size)

    def a_second_passed(self) -> None:
        """
        A function that runs every fucking second
        """
        pass

    def tick(self) -> None:
        pygame.display.flip()
        self.fps = self.clock.get_fps()
        self.current_fps += 1
        if self.fps != 0 and self.current_fps * 1 / self.fps > 1:
            self.current_fps = 0
            self.a_second_passed()
        self.clock.tick()

    def draw_images(self) -> None:
        for image in self.__images:
            image.draw(self.screen)

    def calculate_move(self, value: int) -> float:
        """
        simply nerd stuff but of you're interested it does the VSync job
        :param value:
        :return:
        """
        if self.fps == 0:
            return 0
        return 1 / self.fps * value

    def background_color(self, color: list = []) -> None:
        """
        set background color
        :param color:
        """
        self.screen.fill(color)

    def add_image(self, image: Image) -> None:
        """
        Appends an image to images array
        :param image:
        :return:
        """
        self.__images.append(image)

    def remove_image(self, name: str) -> None:
        """
        Removes a image from images array
        :param name:
        :return:
        """
        for i in range(len(self.__images)):
            image = self.__images[i]
            if image.name == name:
                del self.__images[i]

import pygame
from Game.Object import Object
from Game.Rectangle import Rectangle
from Game.Text import Text, Font


class HealthBar(Object):

    def __init__(self, font: Font, x: float = 0, y: float = 0, width: float = 200, height: float = 200,
                 margin_color: list = [0, 0, 0], text_color: list = [0, 0, 0], bar_color: list = [255, 0, 0], fill_percentage: int = 100,
                 margin: int = 5):
        super().__init__(x, y, width, height)

        self.font = font

        self.margin_color = margin_color
        self.bar_color = bar_color
        self.text_color = text_color
        self.margin = margin
        self.__fill_percentage = fill_percentage
        self.calculate_text()
        

    def calculate_text(self):
        characters = len(str(self.fill_percentage))
        x = self.x + self.width / 2 - characters * self.font.size / 2 + 15
        y = self.y + self.height / 2 - self.font.size / 2
        self.text = Text(self.fill_percentage, x, y, self.font, self.text_color)

    # Margin Color property
    @property
    def margin_color(self) -> list:
        return self.__margin_color

    @margin_color.setter
    def margin_color(self, value: list):
        self.__margin_color = value

    # Bar color property
    @property
    def bar_color(self) -> list:
        return self.__bar_color

    @bar_color.setter
    def bar_color(self, value: list):
        self.__bar_color = value

    # Fill percentage property
    @property
    def fill_percentage(self) -> int:
        return self.__fill_percentage

    @fill_percentage.setter
    def fill_percentage(self, value: int):
        self.__fill_percentage = int(value)
        self.calculate_text()

    # Margin property
    @property
    def margin(self) -> int:
        return self.__margin

    @margin.setter
    def margin(self, value: int):
        self.__margin = value

    def draw(self, screen: pygame.Surface):
        """
        Draws the rectangle
        :param screen:
        """
        pygame.draw.rect(screen, self.margin_color, pygame.Rect(
            self.x, self.y, self.width, self.height))

        # inner rectangle draw
        inner = Rectangle(self.x + self.margin, self.y + self.margin, self.width * self.fill_percentage / 100 - self.margin * 2, self.height - self.margin * 2, self.bar_color)
        inner.draw(screen)
        self.text.draw(screen)

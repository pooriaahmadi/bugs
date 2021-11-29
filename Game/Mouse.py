from Game.Object import Object
import pygame


class Mouse(Object):

    def __init__(self, x: float = 0, y: float = 0, width: float = 0, height: float = 0, tickness: int = 10, color: list = [0, 0, 0]):
        super().__init__(x, y, width, height)

        self.tickness = tickness
        self.color = color

    def draw(self, screen: pygame.Surface):
        """Draws the mouse"""

        rect1 = pygame.Rect(0, 0, self.tickness, self.height)
        rect2 = pygame.Rect(0, 0, self.width, self.tickness)
        rect1.center = self.list_coordinates()
        rect2.center = rect1.center
        pygame.draw.rect(screen, self.color, rect1)
        pygame.draw.rect(screen, self.color, rect2)

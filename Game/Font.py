import pygame

class Font:
    
    def __init__(self, path: str, size: int = 30):
        
        self.path = path        
        self.font = pygame.font.Font(path, size)
        self.size = size

    @property
    def size(self) -> int:
        return self.__size
    
    @size.setter
    def size(self, value: int):
        self.__size = value
        self.font = pygame.font.Font(self.path, value)
import pygame

class Sound:
    
    def __init__(self, path: str, volume: int = 100):
        self.sound = None
        self.path = path
        self.volume = volume
        
    @property
    def path(self) -> str:
        return self.__path
    
    @path.setter
    def path(self, value: str):
        self.__path = value
        self.sound = pygame.mixer.Sound(value)
    
    @property
    def volume(self) -> int:
        return self.__volume
    
    @volume.setter
    def volume(self, value: int):
        self.__volume = value
        self.sound.set_volume(value)

    @property
    def length(self) -> float:
        return self.sound.get_length()

    def play(self, times: int = 1):
        """Playing the sound"""
        self.sound.play(times)
        
    def stop(self):
        """Stopping the sound"""
        self.sound.stop()
        
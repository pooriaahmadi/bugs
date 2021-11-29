from Game.Font import Font

class Text:
    
    def __init__(self, message: str, x: float, y: float, font: Font, color: list = [0,0,0], center=False):
        
        self.x = x
        self.y = y
        
        self.font = font
        self.__color = color
        self.__message = str(message)
        self.rendered = None
        self.render_font()
        if center:
            self.center_text()
        
    # Message property
    @property
    def message(self) -> str:
        return self.__message
    
    @message.setter
    def message(self, value:str):
        self.__message = value
        self.render_font()
    
    # Color property
    @property
    def color(self) -> list:
        return self.__color
    
    @color.setter
    def color(self, value: list):
        self.__color = value
        self.render_font()
        
    @property
    def width(self) -> float:
        characters = len(self.message)
        
        return self.font.size * characters
    
    @property
    def height(self) -> float:
        return self.font.size
    
    def center_text(self):
        characters = len(self.message)
        
        self.x -= self.font.size / 2 * characters / 2
        self.y -= self.font.size / 2
    
    def render_font(self):
        """
        Rendering text
        """
        self.rendered = self.font.font.render(self.message, False, self.color)

    def draw(self, screen):
        """
        Drawing text on the screen
        """
        screen.blit(self.rendered, [self.x, self.y])
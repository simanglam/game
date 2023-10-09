from pygame.sprite import Sprite
from pygame.surface import Surface
from pygame.draw import circle

class Charater(Sprite):
    def __init__(self, size, color):
        Sprite.__init__(self)
        self.surface = Surface(size)
        self.surface.fill(color)

    def render(self):
        pass

class PlayerCharater(Charater):

    def __init__(self, size, color):
        self.color = color
        super().__init__(size, color)
        self.health = 10

        self.rect = self.surface.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        
        self.physical_variable = {
            "x_speed" : 0, 
            "y_speed" : 0, 
            "air" : False
            }

        self.physical_constant = {}

    def render(self):
        circle(self.surface, self.color, (250, 250), 100)

    def get_info(self) -> dict[str : int]:
        return (self, self.physical_variable)

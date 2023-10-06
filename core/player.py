from pygame.sprite import Sprite
from pygame.surface import Surface
from pygame.draw import circle

class Charater(Sprite):
    def __init__(self, size, color):
        self.surface = Surface(size)
        self.surface.fill(color)

class PlayerCharater(Charater):

    def __init__(self, size, color):
        self.color = color
        super().__init__(size, color)
        self.health = 10

    def render(self):
        circle(self.surface, self.color, (250, 250), 100)
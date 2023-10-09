from typing import Any
from pygame.sprite import Sprite

from pygame.surface import Surface
from pygame.image import load
from pygame.draw import rect

from ..player import Charater

class BaseMapObject(Sprite):

    def __init__(self, position: tuple, image = None) -> None:
        Sprite.__init__(self)

        self.screen = Surface((50, 50))

        self.screen.fill((0, 0, 0))

        self.rect = self.screen.get_rect()
        self.rect.x, self.rect.y = position

    def update(self, **kwargs: Any) -> None:
        self.rect.x += kwargs["x"]
        self.rect.y += kwargs["y"]

    def on_top(self, object: Charater):
        object.physical_variable["air"] = False
        object.physical_variable["y_speed"] = 0
        object.rect.bottom = self.rect.top + 2

    def on_side(self, object: Charater):
        object.physical_variable["x_speed"] = 0
        if self.rect.left < object.rect.right and self.rect.left > object.rect.left:
            object.rect.right = self.rect.left - 2
        elif self.rect.right > object.rect.left:
            object.rect.left = self.rect.right + 10

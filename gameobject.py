import os
import pygame

class BaseMapObject(pygame.sprite.Sprite):

    def __init__(self, position: tuple, image = None) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.surface.Surface((50, 50))

        self.image.fill((0, 0, 0))

        self.image = pygame.image.load(os.path.join(".", "resource", "map", "grass", "1.png"))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def on_top(self, object):
        object.direction.y = 0
        object.rect.bottom = self.rect.top

    def under(self, object):
        object.rect.top = self.rect.bottom

    def on_side(self, object):
        if object.direction.x > 0:
            object.rect.right = self.rect.left
        elif object.direction.x < 0:
            object.rect.left = self.rect.right

        #object.direction.x = 0
        #object.abs_xspeed = 0
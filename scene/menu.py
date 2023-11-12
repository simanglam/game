import pygame
from .base import abs_scene
from .level import Level
from gameobject import BaseMapObject

class MenuScene(abs_scene):
    def __init__(self, game, width, height):
        super().__init__(game, width, height)
        self.button = BaseMapObject((width / 2, height * 3 / 4))

    def update(self):
        self.screen.fill('white')
        self.screen.blit(self.button.image, self.button.rect)

        key = pygame.key.get_pressed()
        
        if key[pygame.key.key_code("escape")]:
            pygame.quit()
            exit()

        for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
            if self.button.rect.collidepoint(event.dict['pos']):
                self.exit(Level)
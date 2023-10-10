import json
from typing import Any
import pygame

from level import Level

class Game:

    def __init__(self) -> None:
        self.surface = pygame.display.set_mode((1080, 1080), pygame.FULLSCREEN | pygame.HWSURFACE, vsync=2)
        self.width, self.height = self.surface.get_size()
        pygame.init()
        self.scene = Level(self.width, self.height)
        self.running = True
        self.clock = pygame.time.Clock()
        self.info = pygame.font.Font("Hannotate.ttc", 40)

    def run(self):
        while self.running:
            self.scene.update()
            self.surface.blit(self.scene.screen, (0, 0))
            self.surface.blit(self.info.render(str(self.clock.get_fps()), 1, (0, 0, 0)), (0, 0))
            pygame.display.update()
            self.clock.tick(60)



game = Game()

game.run()
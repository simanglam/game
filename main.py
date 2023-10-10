import json
from typing import Any
import pygame

from level import Level

class Game:

    def __init__(self) -> None:
        pygame.init()
        self.scene = Level()
        self.running = True
        self.surface = pygame.display.set_mode((1080, 1080))
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            self.scene.update()
            self.surface.blit(self.scene.screen, (0, 0))
            pygame.display.update()
            self.clock.tick(30)



game = Game()

game.run()
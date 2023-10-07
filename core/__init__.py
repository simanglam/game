import pygame
from .updater import Updater
from .player import PlayerCharater

class game:
    
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(1, 1)
        self.screen = pygame.display.set_mode((1080, 1080))
        self.width, self.height = self.screen.get_size()

        self.updater = Updater()

        self.updater.register_charater(PlayerCharater((200, 200), (0, 0, 0)))

        self.clock = pygame.time.Clock()

        self.running = True


    def render(self):
        if len(pygame.event.get(pygame.QUIT)):
            self.running = False
            return
        self.updater.update(pygame.event.get())
        self.screen.fill((255, 255, 255))
        for k, v in self.updater.get_information().items():
            self.screen.blit(k.surface, (v["x"], v["y"]))

    def run(self):
        while self.running:
            self.render()
            pygame.display.update()
            self.clock.tick(30)
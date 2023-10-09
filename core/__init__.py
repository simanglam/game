import pygame
from .updater import Updater
from .player import PlayerCharater
from .map.map import MapManger
from .camara import Camara

class game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1080, 1080))
        self.width, self.height = self.screen.get_size()

        self.map = MapManger()

        self.main_charater = PlayerCharater((200, 200), (0, 0, 0))

        self.main_group = pygame.sprite.Group(self.main_charater)

        self.updater = Updater()
        self.updater.register_charater(self.main_charater)
        self.camara = Camara((0, 0, 1080))
        self.updater.register_camara(self.camara)
        self.updater.register_map(self.map)

        self.clock = pygame.time.Clock()
        self.running = True

        self.action = {"w" : False, "a" : False, "s" : False, "d" : False}


    def update_action(self):
        for k in self.action.keys():
            self.action[k] = False
        key = pygame.key.get_pressed()
        
        for k in self.action.keys():
            if key[pygame.key.key_code(k)]:
                self.action[k] = True       

    def render(self):
        if len(pygame.event.get(pygame.QUIT)):
            self.running = False
            pygame.quit()
        self.map.render()
        self.screen.fill((255, 255, 255))

        self.screen.blit(self.map.screen, self.camara.rect)
        print(self.camara.rect, self.main_charater.rect)
        self.screen.blit(self.main_charater.surface, self.main_charater.rect)

    def run(self):
        while self.running:
            self.update_action()
            self.updater.update(self.action, self.map.terrian_group)
            self.render()
            pygame.display.update()
            self.clock.tick(30)
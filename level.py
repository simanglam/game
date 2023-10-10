import pygame
import json

from player import PlayerCharater
from gameobject import BaseMapObject

class Level:

    def __init__(self) -> None:
        self.screen = pygame.surface.Surface((1080, 1080))

        self.map = JsonMapDecoder()
        self.main_charater = PlayerCharater((20, 20), (0, 0, 0))
        self.terrian_group = pygame.sprite.Group()
        self.map.render(self)
        self.world_shift = 0
        self.running = True   

    def scroll_x(self):
        charater = self.main_charater
        charater.relative_speed = charater.abs_speed

        if charater.direction.x < 0 and charater.rect.x < 200:
            self.world_shift = charater.abs_speed
            charater.relative_speed = 0
    
        elif charater.direction.x > 0 and charater.rect.x > 800:
            self.world_shift = -charater.abs_speed
            charater.relative_speed = 0

        else:
            self.world_shift = 0


        self.terrian_group.update(self.world_shift)

    def horizon_collide(self):
        charater = self.main_charater
        charater.rect.x += charater.direction.x * charater.relative_speed
        
        for sprite in self.terrian_group.sprites():
            if sprite.rect.colliderect(charater.rect):
                sprite.on_side(charater)

    def vertical_collide(self):
        charater = self.main_charater
        charater.rect.y += charater.direction.y
        charater.air = True
        charater.apply_gravity(9.8)

        for sprite in self.terrian_group.sprites():
            if sprite.rect.colliderect(charater.rect):
                if charater.direction.y > 0:
                    sprite.on_top(charater)

    def update(self):
        charater = self.main_charater
        charater.update()
        self.scroll_x()
        self.horizon_collide()
        self.vertical_collide()

        self.render()

    def render(self):
        if len(pygame.event.get(pygame.QUIT)):
            self.running = False
            pygame.quit()

        self.screen.fill((255, 255, 255))
        self.terrian_group.draw(self.screen)
        #self.main_charater.draw(self.screen)
        self.screen.blit(self.main_charater.image, self.main_charater.rect)

    
class JsonMapDecoder:

    def __init__(self) -> None:
        self.ground = BaseMapObject((50, 50))

        self.object_mapping = {
            "ground" : BaseMapObject((50, 50))
        }

        self.mapdata = None

        self.decode("./mapdata/level1.json")

    def decode(self, file: str):
        with open(file, "r") as map_file:
            self.mapdata = json.load(map_file)

    def render(self, game):
        for data in self.mapdata["mapdata"]:
            new_terrian = BaseMapObject((data["x"], data["y"]))
            game.terrian_group.add(new_terrian)


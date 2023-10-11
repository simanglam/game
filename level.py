import pygame
import json

from player import PlayerCharater
from gameobject import BaseMapObject

class Level:

    def __init__(self, width, height) -> None:
        self.screen = pygame.surface.Surface((width, height))

        self.map = JsonMapDecoder()
        self.main_charater = PlayerCharater((30, 30), (0, 0, 0))
        self.terrian_group = pygame.sprite.Group()
        self.map.render(self)
        self.world_xshift = 0
        self.world_yshift = 0
        self.running = True   

    def scroll_x(self):
        charater = self.main_charater
        charater.relative_xspeed = charater.abs_xspeed

        if charater.direction.x < 0 and charater.rect.x < 200:
            self.world_xshift = charater.abs_xspeed
            charater.relative_xspeed = 0
    
        elif charater.direction.x > 0 and charater.rect.x > 800:
            self.world_xshift = -charater.abs_xspeed
            charater.relative_xspeed = 0

        else:
            self.world_xshift = 0


        self.terrian_group.update(x = self.world_xshift, y = 0)
        self.horizon_collide()

    def scroll_y(self):
        charater = self.main_charater
        charater.relative_yspeed = charater.abs_yspeed


        if charater.direction.y < 0 and charater.rect.top < 100:
            self.world_yshift = charater.abs_yspeed
            charater.relative_yspeed = 0
    
        elif charater.direction.y > 0 and charater.rect.bottom >= 700:
            self.world_yshift = -charater.abs_yspeed
            charater.rect.bottom = 700
            charater.relative_yspeed = 0

        else:
            self.world_yshift = 0


        self.terrian_group.update(x = 0, y = self.world_yshift)
        self.vertical_collide()


    def horizon_collide(self):
        charater = self.main_charater
        charater.rect.x += charater.direction.x * charater.relative_xspeed
        for sprite in self.terrian_group.sprites():
            if sprite.rect.colliderect(charater.rect):
                sprite.on_side(charater)
                break
                

    def vertical_collide(self):
        self.colide = False
        
        charater = self.main_charater
        charater.apply_gravity(9.8)
        charater.rect.y += charater.direction.y * charater.relative_yspeed

        for sprite in self.terrian_group.sprites():
            if sprite.rect.colliderect(charater.rect):
                if charater.direction.y >= 0:
                    sprite.on_top(charater)
                    self.colide = True
                    break
                elif charater.direction.y < 0:
                    sprite.under(charater)
        if not self.colide and charater.direction.y == 0:
            charater.direction.y = 1

    def update(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.key.key_code("escape")]:
            pygame.quit()
            exit()

        charater = self.main_charater
        charater.update()
        self.scroll_x()
        self.scroll_y()
        #self.horizon_collide()
        #self.vertical_collide()
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


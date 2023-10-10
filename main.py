import json
from typing import Any
import pygame

class Charater(pygame.sprite.Sprite):
    def __init__(self, size, color):
        pygame.sprite.Sprite.__init__(self)
        self.surface = pygame.surface.Surface(size)
        self.surface.fill(color)

    def render(self):
        pass

class PlayerCharater(Charater):

    def __init__(self, size, color):
        self.color = color
        super().__init__(size, color)
        self.health = 10

        self.rect = self.surface.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        self.air = False

        self.action = {"w" : False, "a" : False, "s" : False, "d" : False}
        
        self.direction = pygame.math.Vector2(0, 0)

        self.physical_constant = {}

    def get_input(self):
        for k in self.action.keys():
            self.action[k] = False
        key = pygame.key.get_pressed()
        
        for k in self.action.keys():
            if key[pygame.key.key_code(k)]:
                self.action[k] = True  

    def update(self) -> None:
        self.get_input()
        event_list = self.action
        self.rect.x += self.direction.x
        self.rect.y += self.direction.y

        if self.air:
            self.direction.y += 10 if self.direction.y < 15 else 0

        for k, v in event_list.items():

            match(k):
                case("w"):
                    if v:
                        #if not self.air:
                            #self.air = True
                            self.direction.y -= 2
                case("s"):
                        if v:
                            self.direction.y += 2
                case("d"):
                    if v:
                        self.direction.x +=  20 * ((20 - self.direction.x)/ 20)
                case("a"):
                    if v:
                        self.direction.x -= 20 * ((20 + self.direction.x)/ 20)

        if not event_list["a"] and not event_list["d"]:
            if self.direction.x > 0:
                self.direction.x -= 3 if self.direction.x >= 3 else self.direction.x
            elif self.direction.x < 0: 
                self.direction.x += 3 if self.direction.x <= 3 else self.direction.x
        

    def render(self):
        pygame.draw.circle(self.surface, self.color, (250, 250), 100)

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


class Level:

    def __init__(self) -> None:
        self.screen = pygame.surface.Surface((1080, 1080))

        self.map = JsonMapDecoder()
        self.main_charater = PlayerCharater((20, 20), (0, 0, 0))
        self.terrian_group = pygame.sprite.Group()
        self.map.render(self)
        self.world_shift = 0
        self.running = True   

    def update(self):
        charater = self.main_charater
        print(charater.direction.x, charater.rect.x)
        if charater.direction.x < 0 and charater.rect.x < 200:

            self.world_shift = -charater.direction.x
            charater.direction.x = 0
        elif charater.direction.x > 0 and charater.rect.x > 800:
            self.world_shift = -charater.direction.x
            charater.direction.x = 0

        else:
            charater.direction.x += -self.world_shift
            self.world_shift = 0

        self.terrian_group.update(self.world_shift)
        charater.update()
        
        self.render()

    def render(self):
        if len(pygame.event.get(pygame.QUIT)):
            self.running = False
            pygame.quit()

        self.screen.fill((255, 255, 255))
        self.terrian_group.draw(self.screen)
        self.screen.blit(self.main_charater.surface, self.main_charater.rect)

    
class MapManger:

    def __init__(self, level) -> None:
        self.screen = level.screen

        self.decoder = JsonMapDecoder()
        
        self.terrian_group = pygame.sprite.Group()

    def render(self):
        self.screen.fill((255, 255, 255))
        self.decoder.render(self)

    def scroll_x(self):
        pass


class BaseMapObject(pygame.sprite.Sprite):

    def __init__(self, position: tuple, image = None) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.surface.Surface((50, 50))

        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def update(self, shift):
        self.rect.x += shift

    def on_top(self, object):
        object.physical_variable["air"] = False
        object.physical_variable["y_speed"] = 0
        object.rect.bottom = self.rect.top + 2

    def on_side(self, object):
        object.physical_variable["x_speed"] = 0
        if self.rect.left < object.rect.right and self.rect.left > object.rect.left:
            object.rect.right = self.rect.left - 2
        elif self.rect.right > object.rect.left:
            object.rect.left = self.rect.right + 10


class JsonMapDecoder:

    def __init__(self) -> None:
        self.ground = BaseMapObject((50, 50))

        self.object_mapping = {
            "ground" : BaseMapObject((50, 50))
        }

        self.mapdata = None

        self.decode("./level1.json")

    def decode(self, file: str):
        with open(file, "r") as map_file:
            self.mapdata = json.load(map_file)

    def render(self, game):
        for data in self.mapdata["mapdata"]:
            new_terrian = BaseMapObject((data["x"], data["y"]))
            game.terrian_group.add(new_terrian)

game = Game()

game.run()
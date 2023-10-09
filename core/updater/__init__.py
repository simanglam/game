import pygame

from ..player import Charater

class Updater:
    
    def __init__(self) -> None:
        self.charater_status = {}

    def register_charater(self, charater: Charater):
        self.main_charater: Charater = charater

    def register_camara(self, camara: Charater):
        self.camara: Charater = camara

    def register_map(self, map):
        self.map = map

    def update(self, event_list: dict[str : bool], collusion_list):
        self.camara.update(self.main_charater.physical_variable['x_speed'], self.main_charater.physical_variable['y_speed'])
        self.main_charater.rect.bottom += self.main_charater.physical_variable['y_speed']
        self.main_charater.rect.x += self.main_charater.physical_variable['x_speed']
        # self.map.update(x = self.main_charater.physical_variable['x_speed'], y = self.main_charater.physical_variable['y_speed'])
        if self.main_charater.rect.bottom > 800:
            self.main_charater.physical_variable["air"] = False
            self.main_charater.rect.bottom = 800
            self.main_charater.physical_variable['y_speed'] = 0

        self.collusion_update(collusion_list, event_list)
        self.physical_update(event_list)

    def physical_update(self, event_list: dict):

        if self.main_charater.physical_variable["air"]:
            self.main_charater.physical_variable['y_speed'] += 10 if self.main_charater.physical_variable['y_speed'] < 15 else 0

        for k, v in event_list.items():

            match(k):
                case("w"):
                    if v:
                        if not self.main_charater.physical_variable["air"]:
                            self.main_charater.physical_variable["air"] = True
                            self.main_charater.physical_variable['y_speed'] -= 60
                            self.main_charater.rect.y -= 10
                case("s"):
                        if v:
                            self.main_charater.physical_variable['y_speed'] += 2
                case("d"):
                    if v:
                        self.main_charater.physical_variable['x_speed'] +=  20 * ((20 - self.main_charater.physical_variable['x_speed'])/ 20)
                case("a"):
                    if v:
                        self.main_charater.physical_variable['x_speed'] -= 20 * ((20 + self.main_charater.physical_variable['x_speed'])/ 20)

        if not event_list["a"] and not event_list["d"]:
            if self.main_charater.physical_variable['x_speed'] > 0:
                self.main_charater.physical_variable['x_speed'] -= 3 if self.main_charater.physical_variable['x_speed'] >= 3 else self.main_charater.physical_variable['x_speed']
            elif self.main_charater.physical_variable['x_speed'] < 0: 
                self.main_charater.physical_variable['x_speed'] += 3 if self.main_charater.physical_variable['x_speed'] <= 3 else self.main_charater.physical_variable['x_speed']
        

    def collusion_update(self, collusion_list: pygame.sprite.Group, event_list: dict[str, bool]):
        col = pygame.sprite.spritecollide(self.main_charater, collusion_list, False)
        if len(col):
            for i in col:
                i.on_top(self.main_charater)
        else:
            self.main_charater.physical_variable['air'] = True


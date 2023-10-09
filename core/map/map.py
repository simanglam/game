from ..base import BaseMapObject

from pygame.surface import Surface
from pygame.sprite import Group

import json

class MapManger:

    def __init__(self) -> None:
        self.screen = Surface((2080, 2080))

        self.decoder = JsonMapDecoder()
        
        self.terrian_group = Group()

    def render(self):
        self.screen.fill((255, 255, 255))
        self.decoder.render(self)
    
    def update(self, **argv):
        self.terrian_group.update(x = argv.get("x", 0), y = argv.get("y", 0))




class JsonMapDecoder:

    def __init__(self) -> None:
        self.ground = BaseMapObject((50, 50))

        self.object_mapping = {
            "ground" : BaseMapObject((50, 50))
        }

        self.mapdata = None

        self.decode("./core/map/level1.json")

    def decode(self, file: str):
        with open(file, "r") as map_file:
            self.mapdata = json.load(map_file)

    def render(self, mapm: MapManger):
        for data in self.mapdata["mapdata"]:
            new_terrian = BaseMapObject((data["x"], data["y"]))
            mapm.screen.blit(new_terrian.screen, new_terrian.rect)
            mapm.terrian_group.add(new_terrian)
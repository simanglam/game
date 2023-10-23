import pygame

class Charater(pygame.sprite.Sprite):
    def __init__(self, size, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface(size)
        self.image.fill(color)

    def render(self):
        pass

class PlayerCharater(Charater):

    def __init__(self, size, color):
        self.color = color
        super().__init__(size, color)
        self.health = 10

        self.abs_xspeed = 0
        self.relative_xspeed = 0

        self.abs_yspeed = 0
        self.relative_yspeed = 0

        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        self.air = False

        self.action = {"w" : False, "a" : False, "s" : False, "d" : False}
        
        self.direction = pygame.math.Vector2(0, 1)

        self.physical_constant = {}

    def get_input(self):
        for k in self.action.keys():
            self.action[k] = False
        key = pygame.key.get_pressed()
        
        for k in self.action.keys():
            if key[pygame.key.key_code(k)]:
                self.action[k] = True

    def apply_gravity(self, gravity):
        if self.direction.y < 0:
            self.abs_yspeed -= gravity if self.abs_yspeed > gravity else self.abs_yspeed
            
        elif self.direction.y > 0:
            self.abs_yspeed += gravity if self.abs_yspeed < gravity else 0


    def update(self) -> None:
        self.get_input()
        event_list = self.action

        for k, v in event_list.items():

            match(k):
                case("w"):
                    if v:
                        if self.direction.y == 0:
                            self.direction.y = -1
                            self.abs_yspeed = 60
                case("s"):
                        if v:
                            self.abs_yspeed += self.direction.y * 2
                case("d"):
                    if v:
                        self.direction.x = 1
                case("a"):
                    if v:
                        self.direction.x = -1

        if not event_list["a"] and not event_list["d"]:
            self.abs_xspeed -= 2 if self.abs_xspeed >= 2 else self.abs_xspeed
            if self.abs_xspeed == 0:
                self.direction.x = 0
        else:
            self.abs_xspeed += 15 * ((15 - self.abs_xspeed) / 15)
        if self.abs_yspeed == 0:
                self.direction.y = 1

        
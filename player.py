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

        self.abs_speed = 0
        self.relative_speed = 0

        self.rect = self.image.get_rect()
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

    def apply_gravity(self, gravity):
        if self.air:
            self.direction.y += gravity if self.direction.y < 2*gravity else 0

    def update(self) -> None:
        self.get_input()
        event_list = self.action

        for k, v in event_list.items():

            match(k):
                case("w"):
                    if v:
                        if not self.air:
                            self.air = True
                            self.direction.y -= 75
                case("s"):
                        if v:
                            self.direction.y += 2
                case("d"):
                    if v:
                        self.direction.x = 1
                case("a"):
                    if v:
                        self.direction.x = -1

        if not event_list["a"] and not event_list["d"]:
            self.abs_speed -= 2 if self.abs_speed >= 2 else self.abs_speed
            if self.abs_speed == 0:
                self.direction.x = 0
        else:
            self.abs_speed += 20 * ((20 - self.abs_speed) / 20)
        
from pygame.rect import Rect

class Camara:
    def __init__(self, size: tuple[int, int, int]) -> None:
        self.rect = Rect(size[0], size[1], size[2], size[2])

    def update(self, x_speed, y_speed):
        self.rect.x -= x_speed
        self.rect.y -= y_speed
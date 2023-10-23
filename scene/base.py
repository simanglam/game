import pygame

class abs_scene:

    def __init__(self, game, width, height):
        self.game = game
        self.screen = pygame.surface.Surface((width, height))

    def exit(self, new_scene):
        self.game.scene = new_scene(self.game, self.screen.get_width(), self.screen.get_height())

    def update(self):
        pass


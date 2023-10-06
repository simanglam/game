import pygame


class Updater:
    
    def __init__(self) -> None:
        self.charater_status = {}

    def register_charater(self, charater):
        self.main_charater = charater
        self.charater_status[self.main_charater] = {"x" : 500, "y" : 500}

    def update(self, event_list: list[pygame.event.Event]):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.charater_status[self.main_charater]['x'] -= 1

    def get_information(self):
        return self.charater_status
    
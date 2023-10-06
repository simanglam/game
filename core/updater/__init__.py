import pygame


class Updater:
    
    def __init__(self) -> None:
        self.charater_status = {}

    def register_charater(self, charater):
        self.main_charater = charater
        self.charater_status[self.main_charater] = {"x" : 500, "y" : 500, "x_speed" : 0, "y_speed" : 0}

    def update(self, event_list: list[pygame.event.Event]):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.charater_status[self.main_charater]['y_speed'] -= 100
                    self.charater_status[self.main_charater]['y'] = 549

        self.charater_status[self.main_charater]['y_speed'] -= -9.8
        self.charater_status[self.main_charater]['y'] += self.charater_status[self.main_charater]['y_speed']
        
        if self.charater_status[self.main_charater]['y'] >= 550:
            self.charater_status[self.main_charater]['y'] = 550
            self.charater_status[self.main_charater]['y_speed'] = 0



    def get_information(self):
        return self.charater_status
    
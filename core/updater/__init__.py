import pygame


class Updater:
    
    def __init__(self) -> None:
        self.charater_status = {}

    def register_charater(self, charater):
        self.main_charater = charater
        self.charater_status[self.main_charater] = {
            "x" : 500, 
            "y" : 500, 
            "x_speed" : 0, 
            "y_speed" : 0, 
            "air" : False
            }

    def update(self, event_list: list[pygame.event.Event]):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if not self.charater_status[self.main_charater]["air"]:
                        self.charater_status[self.main_charater]["air"] = True
                        self.charater_status[self.main_charater]['y_speed'] -= 100
                        self.charater_status[self.main_charater]['y'] = 549

                if event.key == pygame.K_DOWN:
                    self.charater_status[self.main_charater]['y_speed'] += 2

                if event.key == pygame.K_RIGHT:
                    self.charater_status[self.main_charater]['x_speed'] +=  20 * ((20 - self.charater_status[self.main_charater]['x_speed'])/ 80)

                if event.key == pygame.K_LEFT:
                    self.charater_status[self.main_charater]['x_speed'] -= 20 * ((20 + self.charater_status[self.main_charater]['x_speed'])/ 80)
                
        if not self.charater_status[self.main_charater]["air"]:
            if self.charater_status[self.main_charater]['x_speed'] > 0:
                self.charater_status[self.main_charater]['x_speed'] -= 3 if self.charater_status[self.main_charater]['x_speed'] >= 3 else self.charater_status[self.main_charater]['x_speed']
            elif self.charater_status[self.main_charater]['x_speed'] < 0:
                self.charater_status[self.main_charater]['x_speed'] += 3  if self.charater_status[self.main_charater]['x_speed'] <= -3 else -self.charater_status[self.main_charater]['x_speed']

        self.charater_status[self.main_charater]['y_speed'] += 9.8
        self.charater_status[self.main_charater]['y'] += self.charater_status[self.main_charater]['y_speed']
        self.charater_status[self.main_charater]['x'] += self.charater_status[self.main_charater]['x_speed']
        
        if self.charater_status[self.main_charater]['y'] >= 550:
            self.charater_status[self.main_charater]["air"] = False
            self.charater_status[self.main_charater]['y'] = 550
            self.charater_status[self.main_charater]['y_speed'] = 0



    def get_information(self):
        return self.charater_status
    
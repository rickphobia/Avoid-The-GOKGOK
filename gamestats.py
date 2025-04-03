import pygame

class Gamestats:
    pygame.init()
    def __init__(self,ai):
        self.screen = ai.screen
        self.settings = ai.settings
        
        self.reset_stats()
        self.high_score = 0 
        self.game_active = False
    def reset_stats(self):
        self.ship_left = self.settings.ship_limit 


    def _check_high_score(self):
        if self.settings.points_count > self.high_score:
            self.high_score = self.settings.points_count 
import pygame
from pygame.sprite import Sprite
from random import randint 
from settings import Setting
class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.setting = Setting()

        filepath = 'images/gokgok.bmp'
        self.image = pygame.image.load(filepath)
        self.image = pygame.transform.scale(self.image,(50,70))
        self.rect = self.image.get_rect()
        self.screen_rect= self.screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 
        self.x = float(self.rect.x)
        

    def update(self):
        self.rect.x += int(self.settings.alien_speed_x* self.settings.alien_dir_x)
        self.rect.y += int(self.settings.alien_speed_y*self.settings.alien_dir_y)


    def check_edges_hori(self):
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True
    # def check_edges_ver(self):
    #     if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <=0:
    #         return True 
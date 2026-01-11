import pygame
import random
import os 
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        base_path = os.path.dirname(__file__)
        filepath = os.path.join(base_path,'images','gokgok.bmp')
        self.image = pygame.image.load(filepath)
        self.image = pygame.transform.scale(self.image,(50,70))
        self.rect = self.image.get_rect()
        self.screen_rect= self.screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.x_direction = random.choice([-1,1])
        

    def update(self):
        self.x += (self.settings.alien_speed_x * self.x_direction)
        self.rect.x = self.x 

        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            self.x_direction *= -1 



        self.y += self.settings.alien_speed_y
        self.rect.y = self.y 
    # def check_edges_ver(self):
    #     if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <=0:
    #         return True 
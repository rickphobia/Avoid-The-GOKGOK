import pygame
from settings import Setting
from pygame.math import Vector2

filepath = 'images/kx_ship.bmp'

class Ship:
    def __init__(self, ai_game):
        """create ship and set position"""
        
        #getting resolution from setting
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = ai_game.settings
        #letting the screen to be a rectangle

        #assign ship image
        self.image = pygame.image.load(filepath)
        self.image = pygame.transform.scale(self.image, (100,134))
        #assign ship as a rectangle 
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect_pos = Vector2(self.rect.topleft)
        self.x = float(self.rect.x)


    def _ship_center(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect_pos = Vector2(self.rect.topleft)
        self.x = float(self.rect.x)
        

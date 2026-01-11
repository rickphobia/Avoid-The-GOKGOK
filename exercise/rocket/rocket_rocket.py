import pygame
from pygame.math import Vector2


class RocketSetting:
    def __init__(self,rocket):
        self.screen = rocket.screen

        filepath = 'exercise/rocket/rocket01.bmp'
        self.pic = pygame.image.load(filepath)
        self.pic = pygame.transform.scale(self.pic,(100,200))
        self.rect = self.pic.get_rect()

        self.rect.center = rocket.screen.get_rect().center
        self.rect_pos =  Vector2(self.rect.topleft)
        



    def blitme(self):
        self.rect.topleft = self.rect_pos
        self.screen.blit(self.pic, self.rect)
        #must be rect_pos otherwise cant move 
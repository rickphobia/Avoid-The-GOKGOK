import pygame
from pygame.sprite import Sprite


class StarImage(Sprite):

    def __init__(self,star):
        super().__init__()
        self.screen = star.screen 
        filepath = 'exercise/star/stars.bmp'
        self.image = pygame.image.load(filepath)
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
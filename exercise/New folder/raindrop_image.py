import pygame
from pygame.sprite import Sprite

class RaindropImage(Sprite):
    def __init__(self, raindrop):
        pygame.init()
        super().__init__()
        self.screen = raindrop.screen
        filepath = 'exercise/raindrops/raindrop.bmp'
        self.image = pygame.image.load(filepath)
        self.image = pygame.transform.scale(self.image,(100,130))
        self.rect = self.image.get_rect()


        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 
        self.y = float(self.rect.y)
    def update(self):
        self.y -= 3
        self.rect.y = self.y 

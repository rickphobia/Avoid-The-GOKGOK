import pygame 
from pygame.math import Vector2
class Health:
    def __init__(self,ai,ship_left):
        pygame.init()
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()
        filepath01 = 'images/empty_health.bmp'
        filepath02 = 'images/health.bmp'
        
        self.image_empty = pygame.image.load(filepath01)
        self.image_empty = pygame.transform.scale(self.image_empty,(70,70))
        self.image_full = pygame.image.load(filepath02)
        self.image_full = pygame.transform.scale(self.image_full,(70,70))
    

        self.pos = Vector2(0,1000)
        self.spacing = 10 

    def blitme(self,ship_left):
        #used chatgpt to help 
        """
        for i inrange(3): it will return 0,1,2
        if ship_left = 3, it will be 3 full hearts
        if 2, it will print 2f and 1 empty 
        """
        for i in range(3):
            pos_x = self.pos.x + i*(self.image_full.get_width()) + self.spacing 
            pos_y = self.pos.y

            if i < ship_left:
                self.screen.blit(self.image_full, (pos_x,pos_y))
            else:
                self.screen.blit(self.image_empty, (pos_x, pos_y))

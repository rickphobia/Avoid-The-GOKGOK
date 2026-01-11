import pygame 
import sys 
from raindrop_image import RaindropImage


class Raindrop:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920,1080))
        self.screen_rect= self.screen.get_rect()
        self.raindrop = pygame.sprite.Group()
        self._raindrop_fleet()
    def _raindrop_fleet(self):
        rd = RaindropImage(self)
        rd_width = rd.rect.width 
        rd_height = rd.rect.height 

        available_space_x = 1920 - 2*rd_width 
        available_space_y = 1080 - 5*rd_height 
        rows = int(available_space_x / 2*rd_width) 
        cols = int(available_space_y /2*rd_height) 

        for row in range(rows):
            for col in range(cols):
                rd.rect.x = (rd_width)(1+2*row) 
                rd.rect.y = (rd_height)(1+2*col) 



    def _update_rd (self):
        self.raindrop.update()

        for rd in self.raindrop.copy():
            if rd.rect.bottom <= 0:
                self.raindrop.remove(rd)
    

    def _update_screen(self):
        self.screen.fill((0,0,0))
        self.raindrop.draw(self.screen)
        pygame.display.flip()

    def run_game(self):
        while True:
            self._update_rd()
            self._update_screen()



if __name__ == '__main__':
    rd = Raindrop()
    rd.run_game()
import pygame 
import sys 
from stars_image import StarImage
from random import randint


class Star:
    def __init__(self):
        pygame.init()
        self.width = 1920 
        self.height= 1080
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen_rect = self.screen.get_rect()
        self.star = pygame.sprite.Group()
        self._stars_fleet()

    def _stars_fleet (self):
       
        star = StarImage(self)
        star_width = star.rect.width 
        star_height = star.rect.height 
        available_space_x = self.width - (2*star_width)
        available_space_y = self.height - (5*star_height) 

        stars_numbers_x = int(available_space_x/star_width -2)
        stars_numbers_y = int(available_space_y/star_height -3)
  
        for star_number_y in range(stars_numbers_y):
            for star_number_x in range(stars_numbers_x):
                self._create_multiple_stars(star_number_x,star_number_y)

    def _create_multiple_stars (self,star_x,star_y):
        star = StarImage(self)
        star_width, star_height = star.rect.size
        star.rect.x = star_width + 2*star_width*star_x
        star.rect.y = star_height + 2*star_height*star_y
       
        self.star.add(star)

    def _update_screen(self):
        self.screen.fill((200,200,200))
        self.star.draw(self.screen)
        pygame.display.flip()

    def _check_event(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                sys.exit 

    def run_game(self):
        while True:
            self._check_event()
            self._update_screen()

if __name__ == '__main__':
    star = Star()
    star.run_game()
    
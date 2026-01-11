import sys
import pygame


class Exercise:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024,600))


    def run_game(self):
        while True:
            self._check_event()
            self._update_screen()
    

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    

    def _update_screen(self):
        self.screen.fill((0,191,255))
        self.kungfupanda()
        pygame.display.flip()

    

    def kungfupanda(self):
        self.pic = pygame.image.load('exercise/kungfupanda/kungfupanda.bmp')
        self.screen_rect = self.screen.get_rect()
        self.pic_rect = self.pic.get_rect() 
        self.pic_rect.midtop = self.pic_rect.midtop
        
        self.screen.blit(self.pic, self.pic_rect)
        
    




if __name__ == '__main__':
    ex = Exercise()
    ex.run_game()
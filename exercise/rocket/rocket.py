import pygame
import sys
from rocket_rocket import RocketSetting
from pygame.math import Vector2


class Rocket:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920,1080))
        self.screen_rect = self.screen.get_rect()
        self.clock =  pygame.time.Clock()
        self.dt = 0


        self.rocket = RocketSetting(self)



    def run_game(self):
        while True:
            self._movement()
            self._update()
            
            self.dt = self.clock.tick(60) / 1000



    



    def _movement(self):
        self.keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
                sys.exit()

        if self.keys[pygame.K_w]:
            self.rocket.rect_pos.y -= 300*self.dt
        

        if self.keys[pygame.K_a]:
            self.rocket.rect_pos.x -= 300*self.dt
        if self.keys[pygame.K_s]:
            self.rocket.rect_pos.y += 300*self.dt
        if self.keys[pygame.K_d]:
            self.rocket.rect_pos.x += 300*self.dt
    

        self.rocket.rect.topleft = self.rocket.rect_pos
        self.rocket.rect.clamp_ip(self.screen_rect)
        self.rocket.rect_pos = Vector2(self.rocket.rect.topleft)
    def _update(self):
        self.screen.fill((200,100,200))
        self.rocket.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ra = Rocket()
    ra.run_game()

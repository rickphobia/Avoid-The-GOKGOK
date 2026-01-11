import pygame
import sys 
from pygame.math import Vector2
from bullet import Bullet
class EventHandler:
    def __init__(self,ai_game,ship,bullets): 
        pygame.init()
        self.screen = ai_game.screen
        self.aliens = ai_game.aliens 
        self.screen_rect  = self.screen.get_rect()
        self.settings = ai_game.settings
        self.ship = ship
        self.dt  = 0 
        self.stats = ai_game.stats
        self.bullets  =  bullets
        self.ai_game = ai_game


    def _fire_bullet(self):
        if len(self.bullets) <= self.settings.bullet_ammount:
            new_bullet  = Bullet(self.ai_game)
            self.bullets.add(new_bullet)


    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit event received - Ignoring for Web compatibility")
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:    
                    self._fire_bullet()

                elif event.key == pygame.K_ESCAPE:
                    self.game_running = False 
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.ship.rect_pos.y -= self.settings.ship_speed*self.dt

        if keys[pygame.K_s]:
            self.ship.rect_pos.y += self.settings.ship_speed*self.dt

        if keys[pygame.K_a]:
            self.ship.rect_pos.x -= self.settings.ship_speed*self.dt

        if keys[pygame.K_d]:
            self.ship.rect_pos.x += self.settings.ship_speed*self.dt

        

        self.ship.rect.topleft =self.ship.rect_pos
        self.ship.rect.clamp_ip(self.screen_rect)
        self.ship.rect_pos  = Vector2(self.ship.rect.topleft)
        


    def _check_play_button(self,mouse_pos):
        button_clicked = self.ai_game.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            pygame.mouse.set_visible(False)
            self.stats.reset_stats()
            self.bullets.empty()
            self.aliens.empty()
            self.settings._initialize_dynamic_settings()
            self.stats.game_active = True




    def blitme(self):
        self.ship.rect.topleft = self.ship.rect_pos
        """draw the ship at current location"""
        self.screen.blit(self.ship.image,self.ship.rect)




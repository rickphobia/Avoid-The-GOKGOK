import pygame
import os 
import random
import asyncio
from settings import Setting
from ship import Ship
from gamestats import Gamestats
from button import Button
from event_handler import EventHandler
from gokgok import Alien
from health import Health
from prep_msg import PrepMsg


class AlienInvasion():
    """initialize game and set game display setting"""  
    def __init__(self):
        pygame.init()
        self.settings = Setting()   
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.settings.width = self.screen.get_width()
        self.settings.height = self.screen.get_height()
        self.clock = pygame.time.Clock()
        basepath = os.path.dirname(__file__)

        self.gokgok = os.path.join(basepath,'images','gokgok.mp3')
        
        try:
            self.hit_sound = pygame.mixer.Sound(self.gokgok)
        except: 
            self.hit_sound = None 

        self.ship = Ship(self)
        self.play_button = Button(self,'Play')
        self.stats = Gamestats(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.event = EventHandler(self,self.ship,self.bullets)
        self.health = Health(self, self.stats.ship_left)
        self.game_running = True 

        self.prep_msg= PrepMsg(self)

        self.spawn_timer = 0.0
        self.level_timer = 0.0
        self.spawn_interval = 0.2

        

        pygame.display.set_caption("Avoid the GOKGOK")

    async def run_game(self):
        """run the game"""
        while self.game_running:
            self.dt = self.clock.tick(60)/1000
            self.event.dt = self.dt
            self.event.check_event()

            if self.game_running: 
                self._update_screen() 

            if self.stats.game_active:
                await self._update_alien()
                self._update_bullets()

            await asyncio.sleep(0)

    async def _update_alien(self):
        self.aliens.update()
        self.spawn_timer += self.dt 
        if self.spawn_timer >= self.spawn_interval:
            self._create_alien_drop() 
            self.spawn_timer = 0 

        self.level_timer += self.dt
        if self.level_timer >= 3.0: 
            self._level_up() 

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._play_gokgok_sound()
            await self._ship_hit()




    def _level_up(self):
        """Advance the level, speed up, and rain harder."""
        self.settings.increase_speed()
        self.level_timer = 0  # Reset the 3s timer
        
        # Make it rain harder! Decrease the spawn interval.
        # Limit it so it doesn't become instant (minimum 0.2s)
        if self.spawn_interval > 0.2:
            self.spawn_interval -= 0.1
            
        print(f"LEVEL UP! Wave {self.settings.game_level}")
    def _play_gokgok_sound (self):
        if self.hit_sound:
            self.hit_sound.play()


    def _create_alien_drop(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        random_x = random.randint(0,self.settings.width - alien_width)

        alien.rect.x = random_x
        alien.x = float(alien.rect.x)

        alien.rect.y = -alien.rect.height 
        alien.y = float(alien.rect.y)
        self.aliens.add(alien)
            
    


    def _change_direction_aliens_hori(self):
        self.settings.alien_dir_x*=-1
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed 


    # def _change_direction_aliens_ver(self):
    #     for alien in self.aliens.sprites():
    #         self.settings.alien_dir_y *=-1

    

    def _update_bullets(self):
        self.bullets.update()   

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._collide_with_bottom()
      

        self._check_collisions_aliens()


    def _check_collisions_aliens(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions: 
            self.settings.points_count += self.settings.alien_points 
            self.stats._check_high_score()

    def _collide_with_bottom(self):
        alien_collide = False 
        #with chatgpt 
        for alien in self.aliens.copy():
            if alien.rect.bottom >= self.screen_rect.bottom:
                self.aliens.remove(alien) 
                alien_collide = True 

            
    def _alien_collide_with_ship(self):
        if pygame.sprite.spritecollide(
            self.ship,
            self.aliens,
            False,
            pygame.sprite.collide_rect_ratio(0.8)
            ):
            print('Ship Hit!!!')
            asyncio.create_task(self._ship_hit())
    

    async def _ship_hit(self):
        if self.stats.ship_left >1: 
            self.stats.ship_left -= 1 
            await asyncio.sleep(1)


            self.aliens.empty()
            self.bullets.empty()
            self.ship._ship_center()
            self._create_alien_drop()
            
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        #refresh the background color as snowhite color
        self.screen.fill(self.settings.bg_color)
        self.health.blitme(self.stats.ship_left)
        self.event.blitme()    


        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)
            #kkeep refreshing the screen(?)             if not self.stats.game_active:
        if not self.stats.game_active:
            self.prep_msg._prep_title()
            self.play_button.display_button()
        self.prep_msg._prep_game_level(f"Wave {self.settings.game_level}")
        self.prep_msg._prep_score(self.settings.points_count)
        self.prep_msg._prep_highscore(self.stats.high_score)

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    asyncio.run(ai.run_game())





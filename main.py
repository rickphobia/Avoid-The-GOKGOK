import pygame
import os 
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

        

        self._create_fleet()
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
        self._check_fleet_edges()
        self.aliens.update()


        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._play_gokgok_sound()
            await self._ship_hit()


    def _play_gokgok_sound (self):
        if self.hit_sound:
            self.hit_sound.play()


    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        available_space_x = self.settings.width- (1*alien_width)
        available_space_y = self.settings.height - (5*self.ship.rect.height) 

        number_rows = int(available_space_y / alien_height) - 4
        numbers_aliens = int(available_space_x / alien_width) -4

        if number_rows <1:
            number_rows = 1

        if numbers_aliens <1:
            numbers_aliens =1    

        for row_number in range(number_rows):
            for alien_number in range(numbers_aliens):
                self._create_multiple_aliens(alien_number,row_number)
            
    def _create_multiple_aliens(self, alien_number,row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        ###idk what does this even mean i only know its for the x position  
        alien.x = alien_width + 2*alien_width*alien_number-5
        alien.y = alien_height + 2*alien_height*row_number-2
        alien.rect.x = alien.x 
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges_hori():
                self._change_direction_aliens_hori()
                break



            # if alien.check_edges_ver():
            #     self._change_direction_aliens_ver()

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
        if not self.aliens: 
            self.bullets.empty() 
            self._create_fleet()
            self.settings.increase_speed()

        self._check_collisions_aliens()

        self._alien_collide_with_ship()

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
        if pygame.sprite.spritecollideany (
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
            self._create_fleet()
            
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





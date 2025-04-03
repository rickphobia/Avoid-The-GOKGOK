import pygame 
from pygame.math import Vector2

class PrepMsg:
    def __init__(self,ai):
        self.screen = ai.screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = ((0,0,0))
        self.hc_color = ((0,0,255))
        self.font = pygame.font.SysFont(None, 60)


    def _prep_score(self,pc):
        pc = str(pc)
        self.msg_image = self.font.render(pc, True, self.text_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.topright = self.screen_rect.topright
        self.screen.blit(self.msg_image, self.msg_rect)

    def _prep_game_level(self,game_level):
        self.msg_image = self.font.render(game_level,True,self.text_color)
        self.msg_rect = self.msg_image.get_rect()
        self.rect_pos = Vector2(0,0)
        self.screen.blit(self.msg_image, self.msg_rect)


    def _prep_highscore(self,hc):
        hc = f"High Score:{hc}" 
        self._show_msg(hc,850,0,self.hc_color)

    def _prep_title(self):
        title = 'Welcum to AVOID THE GOKGOK'
        self._show_msg(title,650,450,self.text_color)



    def _show_msg(self,word,position_x, position_y,color):
        word = str(word)
        self.msg_image = self.font.render(word,True,color )
        self.msg_rect = self.msg_image.get_rect()
        self.screen.blit(self.msg_image, (position_x,position_y))
import pygame
from System import *

class Text():
    def __init__(self):
        # load up a font

        # make a score font / surface
        self.score_font = pygame.font.Font('SuperAdorable-MAvyp.ttf', 40)
        self.black = (0,0,0)
        self.score_surface = self.score_font.render('0',1,self.black)

    #def update_score(self, score=0):
        #self.score_surface = self.score_font.render(f"{score}",1,self.black)

    def draw(self, screen):
        screen.blit(self.score_surface, (20,20))
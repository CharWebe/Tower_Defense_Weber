import pygame
from System import *

class Text():
    def __init__(self):
        # load up a font

        # make a score font / surface
        self.score_font = pygame.font.Font('toxigenesis/toxigenesis bd.otf', 40)
        self.black = (0,0,0)
        self.score = 0
        self.score_surface = self.score_font.render((f'Kills: {self.score}'),1,self.black)

    def update_score(self):
        self.score += 1

    def draw(self, screen):
        self.score_surface = self.score_font.render((f'Kills: {self.score}'),1,self.black)
        screen.blit(self.score_surface, (20,20))
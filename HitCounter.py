import pygame
from System import *

class HitCounter():
    def __init__(self):
        #make a font for the display of how many enemies the tank has hit 
        self.HitCounter_font = pygame.font.Font('Font Folder/toxigenesis bd.otf', 25)
        self.HitCount = 0
        self.HitCounter_surface = self.HitCounter_font.render((f'Kills: {self.HitCount}'),1,'BLACK')

    def update_score(self):
        #adds one to the score
        self.HitCount += 1

    def draw(self, screen):
        #draws Hit counter in the bottom left corner of the screen
        self.HitCounter_surface = self.HitCounter_font.render((f'Kills: {self.HitCount}'),1,'BLACK')
        screen.blit(self.HitCounter_surface, (10,535))
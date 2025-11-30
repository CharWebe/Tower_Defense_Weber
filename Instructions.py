import pygame
from System import *

#Class that puts user instructions on first screen
class Instructions():
    def __init__(self):
        # make instructions font / surface
        self.font = pygame.font.Font('Font Folder/toxigenesis bd.otf', 15)
        self.surface = self.font.render('Use W,A,S,D to move; Space to shoot; Up and Down Arrows to rotate the cannon',1,'BLACK')

    def draw(self, screen):
        screen.blit(self.surface, (125,350))
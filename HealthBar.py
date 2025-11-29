import pygame
from System import *

class HealthBar():
    def __init__(self):
        # load up a font
        self.health_font = pygame.font.Font('toxigenesis/toxigenesis bd.otf', 40)
        self.black = (0,0,0)
        self.health_surface = self.health_font.render('HP:',1,'RED')
        self.hp = 200

    def updatehealth(self):
        if self.hp > 0:
            self.hp -= 50
        elif self.hp <= 0:
            return False
        return True

    def draw(self, screen):
        self.bar_surface = pygame.Surface((self.hp, 20))
        self.bar_surface.fill('RED')
        screen.blit(self.health_surface, (8,555))
        screen.blit(self.bar_surface, (100,573))
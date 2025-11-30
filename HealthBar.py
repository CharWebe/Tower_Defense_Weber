import pygame
from System import *

class HealthBar():
    def __init__(self):
        # load up font
        self.health_font = pygame.font.Font('Font Folder/toxigenesis bd.otf', 40)
        self.health_surface = self.health_font.render('HP:',1,'RED')

        #health points value
        self.hp = 200

    def updatehealth(self):
        #used determine if game is over or not / tank out of health
        if self.hp > 0:
            self.hp -= 50
        elif self.hp <= 0:
            return False
        return True

    def draw(self, screen):
        #make rectangle that represents health remaining
        self.bar_surface = pygame.Surface((self.hp, 20))
        self.bar_surface.fill('RED')

        #blit to bottom left of screen
        screen.blit(self.health_surface, (8,555))
        screen.blit(self.bar_surface, (100,573))
import pygame
from random import randint
from System import *

def make_background():
    #created this background using Tiled app
    #load background for main loop
    b_image = 'kenney_tower-defense-top-down/Tank_background2.png'
    b = pygame.image.load(b_image)
    background = pygame.Surface((WIDTH,HEIGHT))
    background.blit(b,(0,0))
    return background
# Example file showing a basic pygame "game loop"
import pygame
from random import randint
from System import *
from Background import make_background
from Player import Player

# pygame setup
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()
running = True

# make background
background = make_background()

# make a player
player = Player(25,250)

############### TESTING ZONE #######################

####################################################

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # pass the event to our player
        player.check_event(event)


    # update all of our things
    #player.update()

    # draw background
    screen.blit(background,(0,0))

    # RENDER YOUR GAME HERE
    player.draw(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
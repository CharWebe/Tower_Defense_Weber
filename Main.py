# Example file showing a basic pygame "game loop"
import pygame
from random import randint
from System import *
from Background import make_background
from Player import tank
from Text import Text
from Bullet import *

# pygame setup
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()
running = True

# make background
background = make_background()

# make a player
tank = tank(100,335)

# make our title / text instance
text = Text()

############### TESTING ZONE #######################

####################################################

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # pass the event to our player
        tank.check_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # shoot a shell
                tank.shoot()


    # update all of our things
    #player.update()

    # draw background
    screen.blit(background,(0,0))

    dt = clock.tick(60) /1000  # limits FPS to 60

    tank.update()
    text.draw(screen)

    # RENDER YOUR GAME HERE
    tank.draw(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
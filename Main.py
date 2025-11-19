# Example file showing a basic pygame "game loop"
import pygame
from random import randint
from System import *
from Background import make_background
from Player import tank
from Text import Text
from Bullet import *
from Enemy import EnemySoldier
from Button import Button

# pygame setup
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()
running = True

# make background
background = make_background()

#Enemy sprite group
enemy_group = pygame.sprite.Group()

# make a player
tank = tank(100,335,enemy_group)

#Make enemy soldiers
num_enemies = 20
for i in range(num_enemies):
    enemy_group.add(EnemySoldier(tank))

# make our title / text instance
text = Text()
play_button = Button(screen, "Play")
game_active = False

############### TESTING ZONE #######################


####################################################

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_pos):
                game_active = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # shoot a shell
                tank.shoot()

    keys = pygame.key.get_pressed()
    tank.update(keys)
    
    

    # update all of our things
    #player.update()

    # draw background
    screen.blit(background,(0,0))

    if game_active == False:
        play_button.draw_button()

    dt = clock.tick(60) /1000  # limits FPS to 60

    text.draw(screen)
    enemy_group.update()

    # RENDER YOUR GAME HERE
    if game_active:
        tank.draw(screen)
        enemy_group.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
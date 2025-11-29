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
from HealthBar import HealthBar

# pygame setup
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()
running = True

# make background
background = make_background()

#Sprite groups
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
fire_group = pygame.sprite.Group()

# make a player
tank = tank(100,335,enemy_group,fire_group)
player_group.add(tank)

#Make enemy soldiers
num_enemies = 50
for i in range(num_enemies):
    enemy_group.add(EnemySoldier(tank))

# make our title / text instance
score = 0
text = Text()
health_bar = HealthBar()
play_button = Button(screen, "Wave 1")
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
    player_group.update(keys, text, health_bar)
    
    

    # update all of our things
    #player.update()

    # draw background
    screen.blit(background,(0,0))

    if game_active == False:
        play_button.draw_button()

    dt = clock.tick(60) /1000  # limits FPS to 60

    text.draw(screen)
    health_bar.draw(screen)

    # RENDER YOUR GAME HERE
    for t in player_group:
        t.draw(screen)
    if game_active:
        for enemy in enemy_group:
            enemy.update()
            enemy.draw(screen)
        for f in fire_group:
            f.update()
            f.draw(screen)
        text.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
#imports
import pygame
from random import randint
from System import *
from Background import make_background
from Player import tank
from HitCounter import HitCounter
from Bullet import *
from Enemy import EnemySoldier
from Button import Button
from HealthBar import HealthBar
from Instructions import Instructions

# pygame setup/initial display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Brawl")
clock = pygame.time.Clock()

#Variable for 1st while loop
GameOn = True

#round variable
round = 1

#make background
background = make_background()

#Sprite groups
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
fire_group = pygame.sprite.Group()

# make a player
tank = tank(200,300,enemy_group,fire_group)
player_group.add(tank)


HitCount = HitCounter()

while GameOn:
    running = True

    if round == 1:
        #Make enemy soldiers
        num_enemies = 1
        play_button = Button(screen, "Wave 1")
        instructions = Instructions()

    elif round == 2:
        num_enemies = 2
        play_button = Button(screen, "Wave 2")

    elif round == 3:
        num_enemies = 3
        play_button = Button(screen, "Wave 3")

    elif round == 4:
        num_enemies = 4
        play_button = Button(screen, "Wave 4")

    elif round == 5:
        num_enemies = 5
        play_button = Button(screen, "Final Wave")

    elif round == 0:
        play_button = Button(screen, "Ouch!")

    elif round == 6:
        play_button = Button(screen, "You Win!")

    for i in range(num_enemies):
        enemy_group.add(EnemySoldier(tank))

    for e in enemy_group:
        e.upgrade()

    health_bar = HealthBar()
    game_active = False

    ############### TESTING ZONE #######################


    ####################################################

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                GameOn = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button.rect.collidepoint(mouse_pos):
                    game_active = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # shoot a shell
                    tank.shoot()


        keys = pygame.key.get_pressed()
        player_group.update(keys, HitCount, health_bar)
        
        

        # update all of our things
        #player.update()

        # draw background
        screen.blit(background,(0,0))

        if game_active == False:
            play_button.draw_button()
            if round == 1:
                instructions.draw(screen)

        dt = clock.tick(60) /1000  # limits FPS to 60

        HitCount.draw(screen)
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
            HitCount.draw(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

        if round == 6 or round == 0:
            pygame.time.wait(1000)
            Running = False
            GameOn = False
            break

        if len(enemy_group) == 0:
            for f in fire_group:
                pygame.sprite.Sprite.kill(f)
            running = False
            round += 1
        elif len(player_group) == 0:
            running = False
            round = 0
        

pygame.quit()
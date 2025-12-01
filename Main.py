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

#Init 'Score' which I chose hits
HitCount = HitCounter()

#While loop that allows Waves to run
while GameOn:
    running = True

    #Waves 1-?
    if round == 1:
        #Make enemy soldiers, show wave
        num_enemies = 1
        play_button = Button(screen, "Wave 1")
        instructions = Instructions()
    elif round == 2:
        num_enemies = 2
        play_button = Button(screen, "Wave 2")
    elif round < 10 and round != 0:
        num_enemies = int((int(round)**2)/2)
        play_button = Button(screen, f"Wave {round}")
    elif round == 10:
        num_enemies = 50
        play_button = Button(screen, "Final Wave")

    #round when game is over
    elif round == 0:
        play_button = Button(screen, "Ouch!")

    #round that just displays winning screen
    elif round == 11:
        play_button = Button(screen, "You Win!")

    #Add enemies to be spawned in
    for i in range(num_enemies):
        enemy_group.add(EnemySoldier(tank))

    #Add upgrade function later?
    for e in enemy_group:
        e.upgrade()

    #Init tank health
    health_bar = HealthBar()

    #boolean to control whether buttons are showing
    game_active = False

    #Main running loop controls sprite updates
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                GameOn = False
                break
            #Determines whether button has been pressed also from book
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button.rect.collidepoint(mouse_pos):
                    game_active = True
            #shoot shell when space hit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # shoot a shell
                    tank.shoot()

        #update player movement based on buttons pressed
        keys = pygame.key.get_pressed()
        player_group.update(keys, HitCount, health_bar)

        # draw background
        screen.blit(background,(0,0))

        #Draw button on screen if not already pressed
        if game_active == False:
            play_button.draw_button()
            #Draw instructions at beginning
            if round == 1:
                instructions.draw(screen)

        dt = clock.tick(60) /1000  # limits FPS to 60
        clock.tick(60)  # further limits fps, from our chomp game, if I remove speeds up game too much

        #ushow current health and score
        HitCount.draw(screen)
        health_bar.draw(screen)

        # RENDER YOUR GAME HERE
        for t in player_group:
            t.draw(screen)
        if game_active: #draws all of these after button is pressed
            for enemy in enemy_group:
                enemy.update()
                enemy.draw(screen)
            for f in fire_group:
                f.update()
                f.draw(screen)
            HitCount.draw(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        #Final round screen
        if round == 11 or round == 0:
            #Show end screen real quick, then end game
            pygame.time.wait(1000)
            Running = False
            GameOn = False
            break

        #Removes the fire from the screen if all enemies are gone
        if len(enemy_group) == 0:
            #Fire would show before and after button pressed without
            for f in fire_group:
                pygame.sprite.Sprite.kill(f)
            running = False
            #Stars new round
            round += 1
        
        #End game if there is no tank
        if len(player_group) == 0:
            running = False
            round = 0     

pygame.quit()
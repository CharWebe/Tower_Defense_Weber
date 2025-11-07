import pygame
from System import *
from random import randint
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, x=300, y=HEIGHT/2):
        pygame.sprite.Sprite.__init__(self) # init the sprite class
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.base_image = pygame.image.load('kenney_tower-defense-top-down/PNG/Retina/towerDefense_tile249.png')
        self.rect = self.base_image.get_rect()          

    def get_theta(self):
        # get our theta based on our vx and vy
        self.theta = math.atan2(-self.vy,self.vx)

    def update(self):
        # update the rotation
        self.get_theta()
    
    def check_event(self, event):
        # pass an event and check for key moves
        if event.type == pygame.KEYDOWN:
            # we got a keydown event
            # check and see if it was W key
            if event.key == pygame.K_w:
                self.vy += -2
                # player goes up
            # check and see if it was a S key
            if event.key == pygame.K_s:
                # player goes down
                self.vy  += 2
            # move left and right
            if event.key == pygame.K_a:
                # player goes back
                self.vx += -2
            if event.key == pygame.K_d:
                # player goes forward
                self.vx += 2

    
    def draw(self, screen):
        # update our image with rotation
        # check if fish is updside down and flip it
        if self.theta>math.pi/2 or self.theta <-math.pi/2:
            self.image = pygame.transform.flip(self.base_image,0,1)
        else:
            self.image = self.base_image

        self.image = pygame.transform.rotozoom(self.image, math.degrees(self.theta),1)
        self.rect = self.image.get_rect(center=self.rect.center)
        screen.blit(self.image, self.rect)
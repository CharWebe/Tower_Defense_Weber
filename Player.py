import pygame
from System import *
from random import randint
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self) # init the sprite class
        #load the card image and set its rect attribute.
        self.base_image = pygame.image.load('kenney_tower-defense-top-down/PNG/Retina/towerDefense_tile249.png')
        self.rect = self.base_image.get_rect() 

        #Where card starts 
        self.rect.x = posx
        self.rect.y = posy

        self.vx = 0
        self.vy = 0
        self.theta= 90 # rad
                
    
    def check_event(self, event):
        # pass an event and check for key moves
        if event.type == pygame.KEYDOWN:
            # we got a keydown event
            # check and see if it was W key
            if event.key == pygame.K_w:
                self.theta += 2
                # player goes up
            # check and see if it was a S key
            if event.key == pygame.K_s:
                # player goes down
                self.theta  += -2
    
    def draw(self, screen):
        # update our image with rotation
        # check if fish is updside down and flip it
        """
        if self.theta>math.pi/2 or self.theta <-math.pi/2:
            self.image = pygame.transform.flip(self.base_image,0,1)
        else:
            self.image = self.base_image
        """
        #self.image = pygame.transform.rotozoom(self.image)#,math.degrees(self.theta),1)
        #self.rect = self.image.get_rect(center=self.rect.center)
        self.image = pygame.transform.rotozoom(self.image, self.theta,1)
        screen.blit(self.image, self.rect)
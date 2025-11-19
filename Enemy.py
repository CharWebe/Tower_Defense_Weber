import pygame
from System import *
from random import randint
from math import cos, sin, atan2
from Bullet import *

class EnemySoldier(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.vx = randint(-1,-1)
        self.vy = randint(-1,1)
        self.x = WIDTH+100
        self.y = randint(0,HEIGHT)
        self.image = pygame.image.load('kenney_tower-defense-top-down/PNG/Retina/towerDefense_tile245.png')
        self.image =  pygame.transform.flip(self.image, 1, 0)
        self.image = pygame.transform.rotozoom(self.image, 0, .4)
        self.rect = self.image.get_rect()
        self.theta = 0 # angle to player in radians
        self.speed = randint(1,3)  # speed to follow player
        self.player = player

    def get_theta(self):
        # calculate the theta in radians to the player
        delta_x = self.player.posx - self.x
        delta_y = (self.player.posy - self.y)

        # take atan2
        self.theta = atan2(delta_y , delta_x)


    def update(self):
        # update our theta
        self.get_theta()

        # update the position of the soldier
        self.x += self.vx
        self.y += self.vy

        # update the speed of soldier
        self.vx = self.speed * cos(self.theta)
        self.vy = self.speed * sin(self.theta)

        # update the rect
        self.rect.center = (self.x, self.y)
    

    def draw(self, screen):
        screen.blit(self.image, self.rect)
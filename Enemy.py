import pygame
from System import *
import random
import math
from math import cos, sin, atan2
from Bullet import *

class EnemySoldier(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        #init velocity values
        self.vx = 0
        self.vy = 0

        #set spawn point to random postion on perimeter
        side = random.randint(1,4)
        if side == 1:
            self.x = -100
            self.y = random.uniform(0,HEIGHT)
        elif side == 2:
            self.x = random.uniform(0,WIDTH)
            self.y = -100
        elif side == 3:
            self.x = WIDTH+100
            self.y = random.uniform(0,HEIGHT)
        elif side == 4:
            self.x = random.uniform(0,WIDTH)
            self.y = HEIGHT+100

        #init image
        self.original_image = pygame.image.load('kenney_tower-defense-top-down/PNG/Retina/towerDefense_tile245.png')
        self.upgraded_image = pygame.image.load('kenney_tower-defense-top-down/PNG/Retina/towerDefense_tile248.png')
        self.image = self.original_image
        self.rect = self.image.get_rect()

        #variables
        self.speed = random.uniform(1,2)
        self.player = player
        self.hitpoints = 1

    def upgrade(self):
        #function to upgrade enemy making difficulty harder
        self.image = self.upgraded_image
        self.rect = self.image.get_rect()
        self.hitpoints = 3

    def get_theta(self):
        # calculate the theta in radians to the player
        delta_x = self.player.posx - self.x
        delta_y = (self.player.posy - self.y)

        # take atan2
        self.theta = atan2(delta_y , delta_x)

    def update(self):
        # update our theta
        self.get_theta()

        # update the speed of soldier
        self.vx = self.speed * cos(self.theta)
        self.vy = self.speed * sin(self.theta)

        # update the position of the soldier
        self.x += self.vx
        self.y += self.vy

        # update the rect
        angle_degrees = -math.degrees(self.theta)
        rotated_image = pygame.transform.rotozoom(self.original_image, angle_degrees, 0.4)
        self.image = rotated_image
        self.rect = self.image.get_rect(center=(self.x, self.y))

    #draw
    def draw(self, screen):
        screen.blit(self.image, self.rect)
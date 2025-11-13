import pygame
from System import *
from random import randint
from math import cos, sin, radians
from Bullet import *

class tank(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        # init the sprite
        super().__init__()
        self.posx = posx
        self.posy = posy
        self.score = 0
        pygame.sprite.Sprite.__init__(self) # init the sprite class
        #load the card image and set its rect attribute.
        self.cannon_image = pygame.image.load('kenney_tower-defense-top-down/PNG/Retina/towerDefense_tile291.png').convert_alpha()
        self.tank_image = pygame.image.load('kenney_tower-defense-top-down/PNG/Retina/towerDefense_tile268.png').convert_alpha()
        #self.image = self.base_image.convert_alpha()
        self.cannon_rect = self.cannon_image.get_rect() 
        self.tank_rect = self.tank_image.get_rect()

        self.bullet_group = pygame.sprite.Group()

        #Where card starts 
        self.cannon_rect.center = (posx,posy)
        self.tank_rect.center = (posx,posy)

        self.cannon_theta= 0 # rad
        self.tank_theta = 0
        self.vx = 0
        self.vy = 0
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        self.posx += self.vx
        self.posy += self.vy  
        self.bullet_group.update()

    def shoot(self):
        # a new shell is created, and added to shell group
        new_bullet = Bullet(self.posx,self.posy,self.cannon_theta)
        self.bullet_group.add(new_bullet)       
    
    def check_event(self, event):
        # pass an event and check for key moves
        if event.type == pygame.KEYDOWN:
            # we got a keydown event
            # check and see if it was W key
            if event.key == pygame.K_w:
                self.cannon_theta += 30
                # cannon rotates up
            # check and see if it was a S key
            if event.key == pygame.K_s:
                # cannon rotates down
                self.cannon_theta  += -30
            if event.key == pygame.K_DOWN:
                self.tank_theta += -30
            if event.key == pygame.K_UP:
                self.tank_theta += 30

            if event.key == pygame.K_LEFT:
                if self.xspeed > -2.1:
                    self.xspeed += -1
                if self.yspeed < 2.1:
                    self.yspeed += 1

            if event.key == pygame.K_RIGHT:
                if self.xspeed < 2.1:
                    self.xspeed += 1
                if self.yspeed > -2.1:
                    self.yspeed += -1

        self.vx = self.xspeed * cos(radians(self.tank_theta))
        self.vy = self.yspeed * sin(radians(self.tank_theta))
        """
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.vx = 0
                self.vy = 0
            if event.key == pygame.K_RIGHT:
                self.vx = 0
                self.vy = 0
        """
    
    def draw(self, screen):
        # update our image with rotation
        """
        if self.cannon_theta>math.pi/2 or self.cannon_theta <-math.pi/2:
            self.image = pygame.transform.flip(self.base_image,0,1)
        else:
            self.image = self.base_image
        """
        #self.image = pygame.transform.rotozoom(self.image)#,math.degrees(self.cannon_theta),1)
        #self.rect = self.image.get_rect(center=self.rect.center)
        self.rotated_cannon_image = pygame.transform.rotate(self.cannon_image, self.cannon_theta)
        self.cannon_rect = self.rotated_cannon_image.get_rect()
        self.cannon_rect.center = (self.posx,self.posy)
        self.rotated_tank_image = pygame.transform.rotate(self.tank_image, self.tank_theta)
        self.tank_rect = self.rotated_tank_image.get_rect()
        self.tank_rect.center = (self.posx,self.posy)
        screen.blit(self.rotated_tank_image,self.tank_rect)
        screen.blit(self.rotated_cannon_image, self.cannon_rect)
        self.bullet_group.draw(screen)


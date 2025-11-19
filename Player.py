import pygame
from System import *
from math import cos, sin, radians
from Bullet import *

class tank(pygame.sprite.Sprite):
    def __init__(self, posx, posy, enemy_group):
        # init the sprite
        super().__init__()
        self.posx = posx
        self.posy = posy
        self.score = 0
        self.enemy_group = enemy_group
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
        self.speed = 2

    def update(self, keys):  
        if keys[pygame.K_w] and keys[pygame.K_a]:
            self.posy += -self.speed
            self.posx += -self.speed
            self.tank_theta = 135
        elif keys[pygame.K_w] and keys[pygame.K_d]:
            self.posy += -self.speed
            self.posx += self.speed
            self.tank_theta = 45
        elif keys[pygame.K_w]:
            self.posy += -self.speed
            self.tank_theta = 90
        elif keys[pygame.K_s] and keys[pygame.K_d]:
            self.posy += self.speed
            self.posx += self.speed
            self.tank_theta = 315
        elif keys[pygame.K_s] and keys[pygame.K_a]:
            self.posy += self.speed
            self.posx += -self.speed
            self.tank_theta = 225
        elif keys[pygame.K_d]:
            self.posx += self.speed
            self.tank_theta = 0
        elif keys[pygame.K_s]:
            self.posy += self.speed
            self.tank_theta = 270
        elif keys[pygame.K_a]:
            self.posx += -self.speed
            self.tank_theta = 180
        
        if keys[pygame.K_UP]:
            self.cannon_theta += 10
        if keys[pygame.K_DOWN]:
            self.cannon_theta  += -10       
        self.bullet_group.update()

    def shoot(self):
        # a new shell is created, and added to shell group 
        self.tank_rect.center = (self.posx,self.posy)
        new_bullet = Bullet(self.posx,self.posy,self.cannon_theta,self.enemy_group,self.cannon_rect)
        self.bullet_group.add(new_bullet)       
    
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
        self.rotated_cannon_image = pygame.transform.rotozoom(self.cannon_image, self.cannon_theta,.5)
        self.cannon_rect = self.rotated_cannon_image.get_rect()
        self.cannon_rect.center = (self.posx,self.posy)
        self.rotated_tank_image = pygame.transform.rotozoom(self.tank_image, self.tank_theta,.5)
        self.tank_rect = self.rotated_tank_image.get_rect()
        self.tank_rect.center = (self.posx,self.posy)
        screen.blit(self.rotated_tank_image,self.tank_rect)
        screen.blit(self.rotated_cannon_image, self.cannon_rect)
        self.bullet_group.draw(screen)


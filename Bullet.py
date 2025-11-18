import pygame
from math import sin, cos, radians

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, t, enemy_group, cannon_rect):
        # init the sprite
        super().__init__()
        self.x = x
        self.y = y
        self.theta = t
        self.enemy_group = enemy_group
        self.cannon_rect = cannon_rect
        self.bulletspeed = 50

        self.bulletvx =  self.bulletspeed * cos(radians(self.theta))
        self.bulletvy = -self.bulletspeed * sin(radians(self.theta))

        self.image = pygame.image.load('kenney_tower-defense-top-down/PNG/Retina/towerDefense_tile251.png')
        self.image = pygame.transform.rotozoom(self.image, self.theta - 90, 0.5)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        # put in equations of motion for the shell
        self.x += self.bulletvx
        self.y += self.bulletvy
        self.rect.center = (self.x, self.y)

        colliding_enemy = pygame.sprite.spritecollide(self,self.enemy_group,0)
        # check and see if a collision occured
        if colliding_enemy:
            for f in colliding_enemy:
                pygame.sprite.Sprite.kill(f)

    def draw(self,screen):
        screen.blit(self.image, self.cannon_rect.midright)
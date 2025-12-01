#imports
import pygame
from math import sin, cos, radians
from fire import Fire
from HitCounter import *

class Bullet(pygame.sprite.Sprite):
    #x,y, and t match posx, posy, and t of the player
    #loads in enemy_group for collisions
    #cannon_rect needed to launch from right side of cannon
    #Bullet turns into fire on contact
    def __init__(self, x, y, t, enemy_group, cannon_rect, fire_group):
        #init the sprite
        super().__init__()
        #variables carried over
        self.x = x
        self.y = y
        self.theta = t
        self.enemy_group = enemy_group
        self.cannon_rect = cannon_rect
        self.fire_group = fire_group

        #Static speed / initial trajectory
        self.bulletspeed = 50
        self.bulletvx =  self.bulletspeed * cos(radians(self.theta))
        self.bulletvy = -self.bulletspeed * sin(radians(self.theta))

        #missile image set up and surface variables
        missile_image = 'kenney_tower-defense-top-down/PNG/Retina/towerDefense_tile251.png'
        self.image = pygame.image.load(missile_image)
        self.image = pygame.transform.rotozoom(self.image, self.theta - 90, 0.3)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        #Sound variable
        self.hit_sound = pygame.mixer.Sound('kenney_tower-defense-top-down/Audio/explosionCrunch_000.ogg')

    #moves shell across screen
    def update(self,HitCount):
        # put in equations of motion for the shell
        self.x += self.bulletvx
        self.y += self.bulletvy
        self.rect.center = (self.x, self.y)
        #Remove sprite if it goes off screen
        if self.y < 0:
            self.kill()
        if self.y > HEIGHT:
            self.kill()
        if self.x < 0:
            self.kill()
        if self.x > WIDTH:
            self.kill()

        # check and see if a collision occured
        colliding_enemy = pygame.sprite.spritecollide(self,self.enemy_group,0)
        if colliding_enemy:
            #remove shell
            self.kill()
            #play sound
            self.hit_sound.play()
            for c in colliding_enemy:
                collision_pos = self.rect.center
                #removes enemy sprite / blits fire at collision spot
                pygame.sprite.Sprite.kill(c)
                new_fire = Fire(collision_pos, 0.07)
                self.fire_group.add(new_fire)
                #update score
                HitCount.update_score()
            
    #draws to screen
    def draw(self,screen):
        screen.blit(self.image, self.cannon_rect.midright)
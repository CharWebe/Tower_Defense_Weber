import pygame
from System import *
from Bullet import *

class tank(pygame.sprite.Sprite):
    def __init__(self, posx, posy, enemy_group, fire_group):
        # init the sprite
        super().__init__()
        self.posx = posx
        self.posy = posy
        self.score = 0
        self.enemy_group = enemy_group
        self.fire_group = fire_group
        self.bullet_group = pygame.sprite.Group()
        pygame.sprite.Sprite.__init__(self) # init the sprite class

        #load the card image and set its rect attribute.
        self.cannon_image = pygame.image.load('kenney_tower-defense-top-down/PNG/Retina/towerDefense_tile291.png').convert_alpha()
        self.tank_image = pygame.image.load('kenney_tower-defense-top-down/PNG/Retina/towerDefense_tile268.png').convert_alpha()

        #self.image = self.base_image.convert_alpha()
        self.cannon_rect = self.cannon_image.get_rect() 
        self.tank_rect = self.tank_image.get_rect()
        self.rect = self.tank_rect

        #Where card starts 
        self.cannon_rect.center = (posx,posy)
        self.tank_rect.center = (posx,posy)

        #init variables
        self.cannon_theta= 0 # rad
        self.tank_theta = 0
        self.speed = 2

    def update(self, keys, text, health_bar):  
        #move NW
        if keys[pygame.K_w] and keys[pygame.K_a]:
            self.posy += -self.speed
            self.posx += -self.speed
            self.tank_theta = 135
        #move NE
        elif keys[pygame.K_w] and keys[pygame.K_d]:
            self.posy += -self.speed
            self.posx += self.speed
            self.tank_theta = 45
        #Move N
        elif keys[pygame.K_w]:
            self.posy += -self.speed
            self.tank_theta = 90
        #Move SE
        elif keys[pygame.K_s] and keys[pygame.K_d]:
            self.posy += self.speed
            self.posx += self.speed
            self.tank_theta = 315
        #move SW
        elif keys[pygame.K_s] and keys[pygame.K_a]:
            self.posy += self.speed
            self.posx += -self.speed
            self.tank_theta = 225
        #Move E
        elif keys[pygame.K_d]:
            self.posx += self.speed
            self.tank_theta = 0
        #move S
        elif keys[pygame.K_s]:
            self.posy += self.speed
            self.tank_theta = 270
        #move W
        elif keys[pygame.K_a]:
            self.posx += -self.speed
            self.tank_theta = 180

        #Bounce back if the tank hits border
        if self.posy < 0:
            self.posy = 10
        if self.posy > HEIGHT:
            self.posy = HEIGHT - 10
        if self.posx < 0:
            self.posx = 10
        if self.posx > WIDTH:
            self.posx = WIDTH - 10
        
        #Rotate cannon up and down
        if keys[pygame.K_UP]:
            self.cannon_theta += 10
        if keys[pygame.K_DOWN]:
            self.cannon_theta  += -10   

        #update bullet group based on new position
        self.bullet_group.update(text)

        #Set new rect
        self.rect.center = (self.posx, self.posy)

        # check and see if a collision occured
        colliding_enemy = pygame.sprite.spritecollide(self,self.enemy_group,0)
        if colliding_enemy:
            #Check to see if the tank is now at zero health
            if health_bar.updatehealth() == False:
                collision_pos = self.rect.center
                #Tank explode
                new_fire = Fire(collision_pos,.7)
                self.fire_group.add(new_fire)
                self.kill()
                #Kill remaining enemies so screen is clear
                for enemy in self.enemy_group:
                    enemy.kill()
            #basically else, kill the enemy but take damage
            for enemy in colliding_enemy:
                enemy.kill()

    def shoot(self):
        # a new shell is created, and added to shell group 
        self.tank_rect.center = (self.posx,self.posy)
        new_bullet = Bullet(self.posx,self.posy,self.cannon_theta,self.enemy_group,self.cannon_rect,self.fire_group)
        self.bullet_group.add(new_bullet)       
    
    def draw(self, screen):
        # update our image with rotation
        #rotate cannon
        self.rotated_cannon_image = pygame.transform.rotozoom(self.cannon_image, self.cannon_theta,.5)
        self.cannon_rect = self.rotated_cannon_image.get_rect()
        self.cannon_rect.center = (self.posx,self.posy)

        #rotate the base of cannon
        self.rotated_tank_image = pygame.transform.rotozoom(self.tank_image, self.tank_theta,.5)
        self.tank_rect = self.rotated_tank_image.get_rect()
        self.tank_rect.center = (self.posx,self.posy)

        #Draw cannon an tank base
        screen.blit(self.rotated_tank_image,self.tank_rect)
        screen.blit(self.rotated_cannon_image, self.cannon_rect)

        #draw current bullets launched
        self.bullet_group.draw(screen)
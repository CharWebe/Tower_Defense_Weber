import pygame

class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y, t, cannon_rect):
        # init the sprite
        super().__init__()
        self.x = x
        self.y = y
        self.theta = t
        self.cannon_rect = cannon_rect
        self.image = pygame.image.load('kenney_tower-defense-top-down/PNG/Retina/towerDefense_tile298.png')
        self.image = pygame.transform.rotozoom(self.image, self.theta - 90, 0.5)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        # put in equations of motion for the shell
        self.rect.center = (self.x, self.y)

    def draw(self,screen):
        screen.blit(self.image, self.cannon_rect.midright)
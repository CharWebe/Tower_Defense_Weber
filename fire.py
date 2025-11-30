import pygame

#class to make explosion in a collision
class Fire(pygame.sprite.Sprite):
    def __init__(self, center_pos, size):
        # init the sprite
        super().__init__()
        self.size = size
        self.image = pygame.image.load('explosion3.png')
        self.image = pygame.transform.rotozoom(self.image,0,self.size)
        self.rect = self.image.get_rect(center=center_pos)

        #Variable to display explosion for short time
        self.init_time = pygame.time.get_ticks()

    def update(self):
        #Get time
        current_time = pygame.time.get_ticks()
        change_time = current_time - self.init_time

        # If time is over, delete sprite
        if change_time >= 80:
            self.kill()

    #draw to screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)

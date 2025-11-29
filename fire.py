import pygame

class Fire(pygame.sprite.Sprite):
    def __init__(self, center_pos):
        # init the sprite
        super().__init__()
        self.image = pygame.image.load('explosion3.png')
        self.image = pygame.transform.rotozoom(self.image,0,0.07)
        self.rect = self.image.get_rect(center=center_pos)

        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        # put in equations of motion for the shell
        current_time = pygame.time.get_ticks()
        time_elapsed = current_time - self.spawn_time

        # If the duration is exceeded, remove the sprite
        if time_elapsed >= 3:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

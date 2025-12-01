import pygame.font

#Button class from book (p.280)
class Button:

    def __init__(self,screen,msg):
        #import screen
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        #Button variables
        self.width, self.height = 200, 50
        self.button_color = ('BLACK')
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont('toxigenesis/toxigenesis bd.otf', 48)

        #Button rect
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        #Turn Message into rendered image and center text on button
        self.msg_image = self.font.render(msg,True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #Draw blank button then add message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
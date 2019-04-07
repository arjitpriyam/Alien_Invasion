import pygame

class Background():
    def __init__(self, ai_settings, screen):
        super(Background, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.background_image = pygame.image.load("images/back.jpg").convert()
        self.rect = self.background_image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.background_image,[0,0] )#[0, 0])


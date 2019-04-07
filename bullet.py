import pygame
from pygame.sprite import Sprite
import time

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        self.shoot=False
        #self.skip=0.300

    def update(self,ai_settings,screen,ship,bullets):
        self.y -= self.speed_factor
        self.rect.y = self.y

        if self.shoot:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

            if len(bullets) > 0:
                self.shoot=False
                pygame.mixer.music.load('Sounds/shot.wav')
                pygame.mixer.music.play(0)

            for bullet in bullets:
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


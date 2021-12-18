import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, screen, ai_settings, ship):
        super().__init__()
        self.screen = screen

        # setting bullet rect from scratch
        self.rect = pygame.Rect((0, 0, ai_settings.bullet_width,
                                 ai_settings.bullet_height))

        # setting up bullet's location
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor



    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

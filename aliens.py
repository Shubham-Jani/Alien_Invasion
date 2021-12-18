import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, screen, ai_settings):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # loading the image
        self.image = pygame.image.load("alien.bmp")

        # setting up the rect of image
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # setting up the location of the alien

        self.rect.x = self.screen_rect.x
        self.rect.y = self.screen_rect.y

        # setting up the exact location (float)
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

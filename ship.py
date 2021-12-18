import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen

        # loading the image
        self.image = pygame.image.load("battleship.bmp")

        # getting the rect of the ship and screen
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # setting the position of the ship in the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # setting the initial value of moving as False
        self.moving_right = False
        self.moving_left = False

        ''' setting center's position from int to float because we
         want to control the speed of the ship'''
        self.center = float(self.rect.centerx)

    def update(self, ai_settings):
        self.rect.centerx = self.center
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += ai_settings.ship_moving_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= ai_settings.ship_moving_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)

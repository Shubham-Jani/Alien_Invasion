import pygame
from ship import Ship
from settings import Settings
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    ship = Ship(screen)
    aliens = Group()
    bullets = Group()
    gf.create_fleet(ai_settings, screen, aliens)
    while True:
        gf.game_functions(ship, screen, ai_settings, bullets)
        ship.update(ai_settings)
        gf.update_screen(ai_settings, ship, screen, bullets, aliens)


run_game()

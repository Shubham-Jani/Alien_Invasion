import pygame
import sys
from bullet import Bullet
from aliens import Alien


def check_keydown_events(event, ship, screen, ai_settings, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(screen, ai_settings, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def fire_bullets(screen, ai_settings, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(screen, ai_settings, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def game_functions(ship, screen, ai_settings, bullets):
    screen.fill(ai_settings.bg_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, screen, ai_settings, bullets)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def get_numbers_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    numbers_of_aliens_x = int(available_space_x / (2 * alien_width))
    return numbers_of_aliens_x


def create_alien(screen, ai_settings, aliens, alien_number):
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens):
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien_numbers_x = get_numbers_x(ai_settings, alien_width)
    for alien_number in range(alien_numbers_x):
        create_alien(screen, ai_settings, aliens, alien_number)


def update_screen(ai_settings, ship, screen, bullets, aliens):
    screen.fill(ai_settings.bg_color)

    # deleting the bullets that get out of screen
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        bullet.rect.y = bullet.y
        bullet.y -= bullet.speed_factor
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip()

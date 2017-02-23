import sys

import pygame
from pygame.sprite import Group 

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
 # Инициализирует pygame, settings и объект экрана. 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание корабля.
    ship = Ship(ai_settings, screen)
    # Выстрелы
    bullets = Group()
    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # Удаление пуль, вышедших за край экрана.
        gf.update_bullets(bullets) 
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
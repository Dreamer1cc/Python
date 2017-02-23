import sys

import pygame

def check_events():
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """обновляет изображения на экране и отображает новый экран."""
    # При каждом проходе цикла перересовываем экран.
    screen.feel(ai_settings.bg_color)
    ship.blitme()
    # Отображение последнего прорисованного экрана. 
    pygame.display.flip()
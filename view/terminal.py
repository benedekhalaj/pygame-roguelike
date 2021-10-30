import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

BLACK = (0, 0, 0)
RED = (255, 0, 0)


def set_mode():
    """Returns: window object (width * height)"""
    return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def set_caption(caption: str):
    pygame.display.set_caption(caption)


def get_input():
    return pygame.key.get_pressed()


def display_screen(window, player):
    window.fill(BLACK)
    pygame.draw.rect(window, RED, (player['x'], player['y'], player['width'], player['height']))
    pygame.display.update()

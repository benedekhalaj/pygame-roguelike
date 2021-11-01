import pygame

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500


def set_display_caption(caption):
    pygame.display.set_caption(caption)


def set_display_mode():
    return pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

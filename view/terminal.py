import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def set_mode():
    """Returns: window object (width * height)"""
    return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def set_caption(caption: str):
    pygame.display.set_caption(caption)


def get_input():
    return pygame.key.get_pressed()


def display_background(window):
    window.fill(BLACK)


def refresh_display():
    pygame.display.update()


def display_rectangle(window, rectangle):
    rectangle_coordinates = (rectangle.rect.x, rectangle.rect.y, rectangle.rect.width, rectangle.rect.height)
    pygame.draw.rect(window, rectangle.color, rectangle_coordinates)

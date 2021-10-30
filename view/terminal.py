import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


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


def display_screen(window, *entities):
    window.fill(BLACK)
    for entity in entities:
        pygame.draw.rect(window, entity.color, (entity.x, entity.y, entity.width, entity.height))
    pygame.display.update()

import pygame

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500


def set_display_caption(caption):
    pygame.display.set_caption(caption)


def set_display_mode():
    return pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def display_asterix(window, asterix):
    for item in asterix:
        position = (item.rect.x, item.rect.y, item.rect.width, item.rect.height)
        pygame.draw.rect(window, item.color, position)


def refresh_display():
    pygame.display.update()


def display_background(window):
    window.fill((0, 0, 0))

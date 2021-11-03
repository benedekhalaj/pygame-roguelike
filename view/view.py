import pygame

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720


class Colors():
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.MAGENTA = (255, 0, 255)
        self.BROWN = (165, 42, 42)
        self.ORANGE = (255,165,0)

COLORS = Colors()


def set_display_caption(caption):
    pygame.display.set_caption(caption)


def set_display_mode():
    return pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def display_objects(window, objects):
    for item in objects:
        if item.visible is True:
            position = (item.rect.x, item.rect.y, item.rect.width, item.rect.height)
            pygame.draw.rect(window, item.color, position)


def refresh_display():
    pygame.display.update()


def display_background(window):
    window.fill(COLORS.BLACK)


def get_input():
    return pygame.key.get_pressed()

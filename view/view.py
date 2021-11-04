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
        self.ORANGE = (255, 165, 0)
        self.PURPLE = (128, 0, 128)


COLORS = Colors()


def set_display_caption(caption):
    pygame.display.set_caption(caption)


def set_display_mode():
    return pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def display_objects(window, object_types: dict):
    for objects in object_types.values():
        for object in objects:
            position = (object.rect.x, object.rect.y, object.rect.width, object.rect.height)
            if object.visible:
                pygame.draw.rect(window, object.color, position)


def display_player_sword(window, objects):
    sword = objects['player'][0].sword
    if sword.visible:
        sword_position = (sword.rect.x, sword.rect.y, sword.rect.width, sword.rect.height)
        pygame.draw.rect(window, sword.color, sword_position)


def display_player_stat(window, objects):
    stat = objects['player'][0].stat
    window.blit(stat.text, (stat.x, stat.y))


def refresh_display():
    pygame.display.update()


def display_background(window):
    window.fill(COLORS.BLACK)


def get_input():
    return pygame.key.get_pressed()

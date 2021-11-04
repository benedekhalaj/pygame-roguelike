import pygame

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
STAT_WIDTH = WINDOW_WIDTH // 5
STAT_HEIGHT = WINDOW_HEIGHT // 10


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


def display_objects(window, *objects_list: dict):
    for objects in objects_list:
        for objects_list in objects.values():
            for item in objects_list:
                position = (item.rect.x, item.rect.y, item.rect.width, item.rect.height)
                if item.visible:
                    if item.type == 'player':
                        if item.sword.visible:
                            sword_position = (item.sword.rect.x, item.sword.rect.y, item.sword.rect.width, item.sword.rect.height)
                            pygame.draw.rect(window, item.sword.color, sword_position)
                    pygame.draw.rect(window, item.color, position)


def display_texture(window, texture_object):
    texture = texture_object[0]
    pixel_cord = (texture_object[1], texture_object[2])
    window.blit(texture, pixel_cord)


def refresh_display():
    pygame.display.update()


def display_background(window):
    window.fill(COLORS.BLACK)


def get_input():
    return pygame.key.get_pressed()

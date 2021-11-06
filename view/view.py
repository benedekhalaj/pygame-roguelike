import pygame

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900


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
        self.CADETBLUE = (95, 158, 160)
        self.GREY = (192, 192, 192)
        self.SIENNA = (160, 82, 45)
        self.ROSYBROWN = (188, 143, 143)
        self.CRIMSON = (220, 20, 60)


COLORS = Colors()


def display_everything(window, objects):
    display_background(window)
    display_objects(window, objects)
    display_player_stat(window, objects)
    display_player_sword(window, objects)
    refresh_display()


def display_background(window):
    window.fill(COLORS.BLACK)


def display_objects(window, object_types: dict):
    for objects in object_types.values():
        for object in objects:
            if object.visible:
                position = (object.rect.x, object.rect.y, object.rect.width, object.rect.height)
                # pygame.draw.rect(window, object.color, position)
                if object.texture is not None:
                    if type(object.texture) is list:
                        images = len(object.texture)
                        rate = 60//images
                        window.blit(object.texture[object.texture_count//rate], (object.rect.x, object.rect.y))
                    else:
                        window.blit(object.texture, (object.rect.x, object.rect.y))
                else:
                    pygame.draw.rect(window, object.color, position)


def display_player_sword(window, objects):
    player = objects['player'][0]
    sword = player.sword
    if sword.visible:
        sword_position = (sword.rect.x, sword.rect.y, sword.rect.width, sword.rect.height)
        pygame.draw.rect(window, sword.color, sword_position)
        if sword.texture is not None:
            if type(sword.texture) is list:
                images = len(sword.texture)
                rate = player.attack_duration//images
                window.blit(sword.texture[sword.texture_count//rate], (sword.rect.x, sword.rect.y))
            else:
                window.blit(sword.texture, (sword.rect.x, sword.rect.y))


def display_player_stat(window, objects):
    stat = objects['player'][0].stat
    for bar_tuple in stat.bars:
        bar = bar_tuple[0]
        color = bar_tuple[1]
        stat_position = (bar.x, bar.y, bar.width, bar.height)
        pygame.draw.rect(window, color, stat_position)

    for line, text in enumerate(stat.texts.values()):
        y = stat.y + (line * stat.font_size)
        window.blit(text, (stat.x, y))


def refresh_display():
    pygame.display.update()


def set_display_mode():
    return pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def set_display_caption(caption):
    pygame.display.set_caption(caption)


def get_input():
    return pygame.key.get_pressed()

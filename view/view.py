import pygame
<<<<<<< HEAD
from pygame.constants import WINDOWTAKEFOCUS
=======
from pygame import display

from model.player.player import Player
>>>>>>> 2ea4696df6fc5016a638869796d970e8acb869f0

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


def display_everything(window, objects, pause):

    display_background(window)
    display_objects(window, objects)
    display_player_stat(window, objects)
    display_player_sword(window, objects)
    display_enemy_projectile(window, objects)
    if pause:
        display_inventory(window, objects)
    refresh_display()


def display_background(window):
    window.fill(COLORS.BLACK)


def display_object(window, object, fps=60):
    if object.visible:
        #pygame.draw.rect(window, object.color, position)
        if object.texture is not None:
            if type(object.texture) is list:
                images = len(object.texture)
                rate = fps//images
                window.blit(object.texture[object.texture_count//rate], (object.rect.x, object.rect.y))
            else:
                window.blit(object.texture, (object.rect.x, object.rect.y))
        else:
            position = (object.rect.x, object.rect.y, object.rect.width, object.rect.height)
            pygame.draw.rect(window, object.color, position)


def display_objects(window, object_types: dict):
    for objects in object_types.values():
        for object in objects:
            display_object(window, object)


def display_player_sword(window, objects):
    player = objects['player'][0]
    sword = player.sword
    display_object(window, sword, player.attack_duration)


def display_enemy_projectile(window, objects):
    for enemy in objects['enemies']:
        if enemy.type == 'shooter':
            for projectile in enemy.projectiles:
                display_object(window, projectile)


def display_player_stat(window, objects):
    stat = objects['player'][0].stat
    for bar_list in stat.bars:
        bar_rect = bar_list[0][0]
        rect_color = bar_list[0][1]

        stat_position = (bar_rect.x, bar_rect.y, bar_rect.width, bar_rect.height)
        pygame.draw.rect(window, rect_color, stat_position)
        display_stat_texture(window, bar_list[1])

    for line, text in enumerate(stat.texts.values()):
        y = stat.y + (line * stat.font_size)
        window.blit(text, (stat.x, y))


def display_stat_texture(window, bar_texture):
    for texture_piece_tuple in bar_texture:
        picture = texture_piece_tuple[0]
        x = texture_piece_tuple[1]
        y = texture_piece_tuple[2]
        window.blit(picture, (x, y))


def display_inventory(window, objects):
    inventory = objects["player"][0].inventory
    position_x = inventory.position[0]
    position_y = inventory.position[1]
    # pygame.draw.rect(window, inventory.color.WHITE, inventory.position)
    window.blit(inventory.background, (position_x, position_y))
    if inventory.item_icon is not None:
        for item in inventory.item_icon:
            x = item[0][1].x + inventory.gap
            y = item[0][1].y + inventory.gap
            width = item[0][1].width
            height = item[0][1].height
            window.blit(item[0][0], (x, y))
            pygame.draw.rect(window, inventory.color.WHITE, (x, y, width, height), inventory.outer_line_size)
            window.blit(item[1], (x + inventory.outer_line_size, y + inventory.outer_line_size))
            window.blit(item[2], (x, y))



def refresh_display():
    pygame.display.update()


def set_display_mode():
    return pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def set_display_caption(caption):
    pygame.display.set_caption(caption)


def get_input():
    return pygame.key.get_pressed()

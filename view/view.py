import pygame

from view.terminal import SCREEN_HEIGHT, SCREEN_WIDTH

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
        position = (object.rect.x, object.rect.y, object.rect.width, object.rect.height)
        pygame.draw.rect(window, object.color, position)
        if object.texture is not None:
            if type(object.texture) is list:
                images = len(object.texture)
                rate = fps//images
                window.blit(object.texture[object.texture_count//rate], (object.rect.x, object.rect.y))
            else:
                window.blit(object.texture, (object.rect.x, object.rect.y))
        # else:
        #     pygame.draw.rect(window, object.color, position)


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
    bar = stat.bar
    icons = stat.icons

    def display_player_stat_text():
        texts = stat.texts
        for line, text_tuple in enumerate(texts.items()):
            y = stat.y + (line * stat.font_size)
            if text_tuple[0] != "health":
                y += stat.line_corrigate + stat.y
            else:
                y += stat.line_corrigate / 2
            window.blit(text_tuple[1], (stat.x, y))

    def display_player_stat_bar():

        def display_stat_bar_texture(window, bar_texture):
            for texture_piece_tuple in bar_texture:
                picture = texture_piece_tuple[0]
                x = texture_piece_tuple[1]
                y = texture_piece_tuple[2] + stat.y
                window.blit(picture, (x, y))

        bar_rect = bar[0][0]
        rect_color = bar[0][1]

        stat_position = (bar_rect.x, bar_rect.y + stat.y, bar_rect.width, bar_rect.height)
        pygame.draw.rect(window, rect_color, stat_position)
        display_stat_bar_texture(window, bar[1])

    def display_player_stat_icon():
        for icon_list in icons:
            icon = icon_list[0]
            coordinate = icon_list[1]
            window.blit(icon, coordinate)

    display_player_stat_bar()
    display_player_stat_text()
    display_player_stat_icon()


def display_inventory(window, objects):
    inventory = objects["player"][0].inventory
    position_x = inventory.position[0]
    position_y = inventory.position[1]
    window.blit(inventory.background, (position_x, position_y))
    if inventory.item_icon is not None:
        for item in inventory.item_icon:
            x = item[0][1].x + inventory.gap
            y = item[0][1].y + inventory.gap
            width = item[0][1].width
            height = item[0][1].height
            window.blit(item[0][0], (x, y))
            pygame.draw.rect(window, inventory.outer_line_color, (x, y, width, height), inventory.outer_line_size)
            window.blit(item[2], (x + inventory.move_icon + inventory.resize_picture, y + inventory.move_icon + inventory.resize_picture))
            window.blit(item[1], (x + inventory.outer_line_size, y + inventory.outer_line_size))


def refresh_display():
    pygame.display.update()


def set_display_mode():
    return pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def set_display_caption(caption):
    pygame.display.set_caption(caption)


def get_input():
    return pygame.key.get_pressed()


def display_menu(window, text):
    window.blit(text, (0, 0))

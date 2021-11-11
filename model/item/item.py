from pygame import color
from model import data_manager
import pygame


class Sword():
    def __init__(self, texture_id, position: tuple, file_path: str, character_name, colors: object):
        self.type = 'sword'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = create_texture(file_path)
        self.color = colors.PURPLE
        self.texture_id = texture_id
        self.visible = True


class Key():
    def __init__(self, texture_id, position: tuple, file_path: str, colors: object):
        self.type = 'key'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = create_texture(file_path)
        self.color = colors.MAGENTA
        self.texture_id = texture_id
        self.visible = True


class Health_Potion():
    def __init__(self, texture_id, position: tuple, file_path: str, colors: object):
        self.type = 'health_potion'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = create_texture(file_path)
        self.color = colors.CRIMSON
        self.texture_id = texture_id
        self.visible = True


class Chest():
    def __init__(self, texture_id, position: tuple, file_path: str, colors: object):
        self.type = 'chest'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = create_texture(file_path)
        self.color = colors.GREEN
        self.texture_id = texture_id
        self.visible = True


class Floor():
    def __init__(self, texture_id, position: tuple, file_path: str, colors: object):
        self.type = 'floor'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = create_texture(file_path)
        self.color = colors.WHITE
        self.texture_id = texture_id
        self.visible = True


class Wall():
    def __init__(self, texture_id, position: tuple, file_path: str, colors: object):
        self.type = 'wall'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = create_texture(file_path)
        self.color = colors.BLUE
        self.texture_id = texture_id
        self.visible = True


class Door():
    def __init__(self, texture_id, position: tuple, file_path, colors: object):
        self.type = "door"
        self.texture_id = texture_id
        self.position = position
        self.textures = self.get_textures_file_paths()
        self.rect = pygame.Rect(self.position[0], self.position[1], self.position[2], self.position[3])
        self.look_up = None
        self.look_down = None
        self.look_left = None
        self.Loor_right = None
        self.texture = create_texture(file_path)
        self.closed_color = colors.SIENNA
        self.opened_color = colors.ROSYBROWN
        self.color = self.closed_color
        self.status = "closed"
        self.visible = True

    def get_textures_file_paths(self):
        path_name = ""

        if self.texture_id == '61' or self.texture_id == '66':
            if self.texture_id == '66':
                path_name = "New_Map_"
            self.position = (self.position[0], self.position[1], self.position[2] * 2, self.position[3])
            self.look_up = f"{path_name}model/map/textures/Door/skull_gate/horizontal_DOWN_look_up.png"
            self.look_down = f"{path_name}model/map/textures/Door/skull_gate/horizontal_DOWN_look_down.png"
            self.look_left = f"{path_name}model/map/textures/Door/skull_gate/horizontal_DOWN_look_left.png"
            self.Loor_right = f"{path_name}model/map/textures/Door/skull_gate/horizontal_DOWN_look_right.png"

        elif self.texture_id == '62' or self.texture_id == '68':
            if self.texture_id == '68':
                path_name = "New_Map_"
            self.position = (self.position[0], self.position[1], self.position[2] * 2, self.position[3])
            self.look_up = f"{path_name}model/map/textures/Door/skull_gate/horizontal_UP_look_up.png"
            self.look_down = f"{path_name}model/map/textures/Door/skull_gate/horizontal_UP_look_down.png"
            self.look_left = f"{path_name}model/map/textures/Door/skull_gate/horizontal_UP_look_left.png"
            self.Loor_right = f"{path_name}model/map/textures/Door/skull_gate/horizontal_UP_look_right.png"

        elif self.texture_id == '63' or self.texture_id == '67':
            if self.texture_id == '67':
                path_name = "New_Map_"
            self.position = (self.position[0], self.position[1], self.position[2], self.position[3] * 2)
            self.look_up = f"{path_name}model/map/textures/Door/skull_gate/vertical_LEFT_look_up.png"
            self.look_down = f"{path_name}model/map/textures/Door/skull_gate/vertical_LEFT_look_down.png"
            self.look_left = f"{path_name}model/map/textures/Door/skull_gate/vertical_LEFT_look_left.png"
            self.Loor_right = f"{path_name}model/map/textures/Door/skull_gate/vertical_LEFT_look_right.png"

        elif self.texture_id == '64' or self.texture_id == '65':
            if self.texture_id == '65':
                path_name = "New_Map_"
            self.position = (self.position[0], self.position[1], self.position[2], self.position[3] * 2)
            self.look_up = f"{path_name}model/map/textures/Door/skull_gate/vertical_RIGHT_look_up.png"
            self.look_down = f"{path_name}model/map/textures/Door/skull_gate/vertical_RIGHT_look_down.png"
            self.look_left = f"{path_name}model/map/textures/Door/skull_gate/vertical_RIGHT_look_left.png"
            self.Loor_right = f"{path_name}model/map/textures/Door/skull_gate/vertical_RIGHT_look_right.png"

    def update_color(self):
        if self.status == "opened":
            self.visible = False
            self.color = self.opened_color
        else:
            self.color = self.closed_color


def create_texture(file_path):
    if file_path is not None:
        return pygame.image.load(file_path)
    else:
        return None

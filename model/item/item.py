from pygame import color
from model import data_manager
import pygame


class Sword():
    def __init__(self, position: tuple, colors: object):
        self.type = 'sword'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = data_manager.open_image('model/map/textures/items/shortsword.png')
        self.color = colors.PURPLE
        self.visible = True


class Key():
    def __init__(self, position: tuple, colors: object):
        self.type = 'key'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = data_manager.open_image('model/map/textures/items/key.png')
        self.color = colors.MAGENTA
        self.visible = True


class Health_Potion():
    def __init__(self, position: tuple, colors: object):
        self.type = 'health_potion'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = pygame.image.load('model/map/textures/items/potion.png')
        self.color = colors.CRIMSON
        self.visible = True


class Chest():
    def __init__(self, position: tuple, colors: object):
        self.type = 'chest'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = data_manager.open_image('model/map/textures/items/chest_closed.png')
        self.color = colors.GREEN
        self.visible = True


class Floor():
    def __init__(self, position: tuple, colors: object):
        self.type = 'floor'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = pygame.image.load("model/map/textures/terrain/tiles.png")
        self.color = colors.WHITE
        self.visible = True


class Wall():
    def __init__(self, position: tuple, direction: str, colors: object):
        self.type = 'wall'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.direction = direction
        self.texture = self.create_texture(colors)
        self.color = colors.BLUE
        self.visible = True

    def create_texture(self, colors):
        if self.direction == "Horizontal_Wall":
            self.color = colors.BLUE
            return pygame.image.load('model/map/textures/terrain/wall_horizontal.png')
        elif self.direction == "Vertical_Wall":
            self.color = colors.YELLOW
            return pygame.image.load('model/map/textures/terrain/wall_vertical.png')
        else:
            return None


class Door():
    def __init__(self, position: tuple, colors: object):
        self.type = "door"
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3] * 2)
        self.texture = None
        self.closed_color = colors.SIENNA
        self.opened_color = colors.ROSYBROWN
        self.color = self.closed_color
        self.status = "closed"
        self.visible = True

    def update_color(self):
        if self.status == "opened":
            self.color = self.opened_color
        else:
            self.color = self.closed_color

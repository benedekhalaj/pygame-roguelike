from pygame import color
from model import data_manager
import pygame


class Sword():
    def __init__(self, position: tuple, direction: str, colors: object):
        self.type = 'sword'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = create_texture(direction)
        self.color = colors.PURPLE
        self.visible = True


class Key():
    def __init__(self, position: tuple, direction: str, colors: object):
        self.type = 'key'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = create_texture(direction)
        self.color = colors.MAGENTA
        self.visible = True


class Health_Potion():
    def __init__(self, position: tuple, direction: str, colors: object):
        self.type = 'health_potion'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = create_texture(direction)
        self.color = colors.CRIMSON
        self.visible = True


class Chest():
    def __init__(self, position: tuple, colors: object):
        self.type = 'chest'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = None
        self.color = colors.GREEN
        self.visible = True


class Floor():
    def __init__(self, position: tuple, direction: str, colors: object):
        self.type = 'floor'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = create_texture(direction)
        self.color = colors.WHITE
        self.visible = True


class Wall():
    def __init__(self, position: tuple, direction: str, colors: object):
        self.type = 'wall'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = create_texture(direction)
        self.color = colors.BLUE
        self.visible = True


class Door():
    def __init__(self, position: tuple, direction: str, colors: object):
        self.type = "door"
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3] * 2)
        self.texture = create_texture(direction)
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


def create_texture(name):
    # Walls
    if name == "wall_top":
        pygame.image.load("model/map/textures/terrain/wall_top.png")
    elif name == "wall_bottom":
        pygame.image.load("model/map/textures/terrain/wall_bottom.png")
    elif name == "wall_left":
        pygame.image.load("model/map/textures/terrain/wall_left.png")
    elif name == "wall_right":
        pygame.image.load("model/map/textures/terrain/wall_right.png")
    elif name == "wall_horizontal":
        pygame.image.load("model/map/textures/terrain/wall_horizontal.png")
    elif name == "wall_vertical":
        pygame.image.load("model/map/textures/terrain/wall_vertical.png")
    elif name == "wall_corner_lb":
        pygame.image.load("model/map/textures/terrain/wall_corner_lb.png")
    elif name == "wall_corner_lt":
        pygame.image.load("model/map/textures/terrain/wall_corner_lt.png")
    elif name == "wall_corner_rb":
        pygame.image.load("model/map/textures/terrain/wall_corner_rb.png")
    elif name == "wall_corner_rt":
        pygame.image.load("model/map/textures/terrain/wall_corner_rt.png")
    elif name == "wall_end_top":
        pygame.image.load("model/map/textures/terrain/wall_end_top.png")
    elif name == "wall_end_bottom":
        pygame.image.load("model/map/textures/terrain/wall_end_bottom.png")
    elif name == "wall_end_left":
        pygame.image.load("model/map/textures/terrain/wall_end_left.png")
    elif name == "wall_end_right":
        pygame.image.load("model/map/textures/terrain/wall_end_right.png")
    # Items
    elif name == "health_potion":
        pygame.image.load("model/map/textures/items/health_potion.png")
    elif name == "":
        pygame.image.load("")
    elif name == "":
        pygame.image.load("")
    elif name == "":
        pygame.image.load("")
    elif name == "":
        pygame.image.load("")
    else:
        return None

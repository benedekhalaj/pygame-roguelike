from model import data_manager, util
import pygame


class Rectangle():
    def __init__(self, color, position):
        self.color = color
        self.x = position[0]
        self.y = position[1]
        self.width = position[2]
        self.height = position[3]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.visible = True


class Key():
    def __init__(self, color, position):
        self.type = 'key'
        self.color = color
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.visible = True


def create_rectangles(color, screen_width):
    obstacles = []
    size = 25
    for index in range(0, screen_width, size):
        obstacles.append(Rectangle(color, (index, 0, size, size)))
        obstacles.append(Rectangle(color, (0, index, size, size)))
        obstacles.append(Rectangle(color, (index, screen_width - size, size, size)))
    return obstacles


def create_keys(color):
    keys = []
    keys.append(Key(color, (400, 100, 20, 20)))
    keys.append(Key(color, (400, 200, 20, 20)))
    keys.append(Key(color, (400, 400, 20, 20)))
    keys.append(Key(color, (150, 400, 20, 20)))
    return keys

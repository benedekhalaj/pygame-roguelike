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

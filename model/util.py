import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player():
    def __init__(self, position: tuple, color):
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color


class Wall():
    def __init__(self, position, color):
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color


class Chest():
    def __init__(self, position, color):
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color


class Floor():
    def __init__(self, position, color):
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color

from model import data_manager
import pygame


class Sword():
    def __init__(self, position: tuple, color: tuple):
        self.type = 'sword'
        self.color = color
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.visible = True


class Key():
    def __init__(self, position: tuple, color: tuple):
        self.type = 'key'
        self.color = color
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.visible = True


class Health_Potion():
    def __init__(self, position: tuple, color: tuple):
        self.type = 'health_potion'
        self.color = color
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.visible = True


class Chest():
    def __init__(self, position: tuple, color: tuple):
        self.type = 'chest'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color
        self.visible = True


class Floor():
    def __init__(self, position: tuple, color: tuple):
        self.type = 'floor'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color
        self.visible = True


class Wall():
    def __init__(self, position: tuple, color: tuple):
        self.type = 'wall'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color
        self.visible = True


class Door():
    def __init__(self, position: tuple, color: tuple):
        self.type = "door"
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3] * 2)
        self.status = "closed"
        self.color = color
        self.visible = True

from types import coroutine
from model import data_manager, classes
import pygame


class Player():
    def __init__(self, position: tuple, color):
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color

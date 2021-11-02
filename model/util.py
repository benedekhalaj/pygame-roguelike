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
        self.velocity = 10
        self.type = 'player'

    def move_left(self, asterix):
        for item in asterix:
            item.rect.x += self.velocity

    def move_right(self, asterix):
        for item in asterix:
            item.rect.x -= self.velocity

    def move_up(self, asterix):
        for item in asterix:
            item.rect.y += self.velocity

    def move_down(self, asterix):
        for item in asterix:
            item.rect.y -= self.velocity

    def set_center(self, screen_size):
        screen_width = screen_size[0]
        screen_height = screen_size[1]
        x = screen_width / 2 - self.rect.width / 2
        y = screen_height / 2 - self.rect.height / 2
        self.rect.x = x
        self.rect.y = y




class Wall():
    def __init__(self, position, color):
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color
        self.type = 'wall'


class Chest():
    def __init__(self, position, color):
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color
        self.type = 'chest'


class Floor():
    def __init__(self, position, color):
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color
        self.type = 'floor'

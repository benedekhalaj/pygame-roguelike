import pygame


class Player():
    def __init__(self, position: tuple, color):
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color
        self.velocity = 4
        self.type = 'player'
        self.inventory = Inventory()

    def move(self, asterix, x_direction, y_direction):
        if x_direction != 0:
            self.move_single_axis(asterix, x_direction, 0)
        if y_direction != 0:
            self.move_single_axis(asterix, 0, y_direction)

    def move_single_axis(self, asterix, x_direction, y_direction):
        collide = False
        self.rect.x += x_direction
        self.rect.y += y_direction

        for item in asterix:
            if item.type == 'wall':
                if self.rect.colliderect(item.rect):
                    if x_direction > 0:
                        self.rect.right = item.rect.left
                    if x_direction < 0:
                        self.rect.left = item.rect.right
                    if y_direction > 0:
                        self.rect.bottom = item.rect.top
                    if y_direction < 0:
                        self.rect.top = item.rect.bottom
                    collide = True
        if not collide:
            for item in asterix:
                item.rect.x -= x_direction
                item.rect.y -= y_direction


class Inventory():
    def __init__(self):
        self.keys = 0
        self.keys_limit = 99
        self.health_potions = 0
        self.health_potions_limit = 1

    def add_key(self):
        if self.keys < self.keys_limit:
            self.keys += 1

    def add_health_potion(self):
        if self.health_potions < self.health_potions_limit:
            self.health_potions += 1


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

from model import data_manager, util
import random
import pygame


class Player():
    def __init__(self, color):
        self.name = 'Nick'
        self.color = color
        self.x = 200
        self.y = 200
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.default_velocity = 3
        self.sprint_velocity = 5
        self.velocity = self.default_velocity
        self.visible = True

    def move(self, obstacles, dx, dy):
        if dx != 0:
            self.move_single_axis(obstacles, dx, 0)
        if dy != 0:
            self.move_single_axis(obstacles, 0, dy)

    def move_single_axis(self, obstacles, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                if dx > 0:
                    self.rect.right = obstacle.rect.left
                if dx < 0:
                    self.rect.left = obstacle.rect.right
                if dy > 0:
                    self.rect.bottom = obstacle.rect.top
                if dy < 0:
                    self.rect.top = obstacle.rect.bottom

    def sprint(self):
        self.velocity = self.sprint_velocity

    def walk(self):
        self.velocity = self.default_velocity

    def pick_up_key(self, inventory, key):
        if self.rect.colliderect(key.rect) and key.visible is True:
            inventory.keys += 1
            key.visible = False
            print(inventory.keys)


class Inventory():
    def __init__(self):
        self.keys = 0

    def add_key(self):
        self.keys += 1

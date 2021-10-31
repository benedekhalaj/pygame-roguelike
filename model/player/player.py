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
        self.velocity = 5

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

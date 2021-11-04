from model import data_manager
import pygame


class Enemy():
    def __init__(self, position: tuple, color: tuple):
        self.type = "enemy"
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color
        self.visible = True
        self.velocity = 14
        self.count = 0
        self.count_direction = 60
        self.count_limit = self.count_direction * 2

    def move(self):
        if self.count <= self.count_direction:
            self.rect.x += self.velocity
        elif self.count > self.count_direction:
            self.rect.x -= self.velocity
        if self.count > self.count_limit:
            self.count = 0
        else:
            self.count += 1

    def take_damage(self, objects: dict):
        for player in objects["player"]:
            if player.sword.visible:
                if self.rect.colliderect(player.sword.rect):
                    print('hello')

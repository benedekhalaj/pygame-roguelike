from model import data_manager
import pygame


class Standard_Enemy():
    def __init__(self, position: tuple, colors: dict, direction):
        self.type = "enemy"
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = colors.BROWN
        self.visible = True
        self.velocity = 14
        self.count = 0
        self.direction = direction[0]
        self.count_direction = direction[1]
        self.count_limit = self.count_direction * 2
        self.visible = True

    def move(self):
        if self.count <= self.count_direction:
            if self.direction == 'right':
                self.rect.x += self.velocity
            elif self.direction == 'left':
                self.rect.x -= self.velocity
            elif self.direction == 'down':
                self.rect.y += self.velocity
            elif self.direction == 'up':
                self.rect.y -= self.velocity
        elif self.count > self.count_direction:
            if self.direction == 'right':
                self.rect.x -= self.velocity
            elif self.direction == 'left':
                self.rect.x += self.velocity
            elif self.direction == 'down':
                self.rect.y -= self.velocity
            elif self.direction == 'up':
                self.rect.y += self.velocity

        self.set_count()

    def set_count(self):
        if self.count > self.count_limit:
            self.count = 0
        else:
            self.count += 1

    def take_damage(self, objects: dict):
        for player in objects["player"]:
            if player.sword.visible:
                if self.rect.colliderect(player.sword.rect):
                    self.visible = False

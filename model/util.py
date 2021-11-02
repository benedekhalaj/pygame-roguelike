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

    def check_collision(self, asterix):
        for item in asterix:
            if item.type != 'floor' and item.type != 'player' and self.rect.colliderect(item.rect):
                return True
        return False

    def move_everything_left(self, asterix):
        collide = self.check_collision(asterix)
        for item in asterix:
            item.rect.x -= self.velocity


    def move_everything_right(self, asterix):
        collide = self.check_collision(asterix)
        for item in asterix:
            item.rect.x += self.velocity

    def move_everything_up(self, asterix):
        collide = self.check_collision(asterix)
        for item in asterix:
            item.rect.y -= self.velocity


    def move_everything_down(self, asterix):
        collide = self.check_collision(asterix)
        for item in asterix:
            item.rect.y += self.velocity

    def set_center(self, screen_size):
        screen_width = screen_size[0]
        screen_height = screen_size[1]
        x = screen_width / 2 - self.rect.width / 2
        y = screen_height / 2 - self.rect.height / 2
        self.rect.x = x
        self.rect.y = y

        # for obstacle in entities['obstacles']:
        #     if self.rect.colliderect(obstacle.rect):
        #         if dx > 0:
        #             self.rect.right = obstacle.rect.left
        #         if dx < 0:
        #             self.rect.left = obstacle.rect.right
        #         if dy > 0:
        #             self.rect.bottom = obstacle.rect.top
        #         if dy < 0:
        #             self.rect.top = obstacle.rect.bottom




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

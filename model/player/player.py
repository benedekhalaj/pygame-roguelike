from model import data_manager, util
import random
import pygame


class Player():
    def __init__(self, color, screen_size):
        self.name = 'Nick'
        self.color = color
        self.width = 50
        self.height = 50
        self.x = screen_size[0] / 2 - self.width / 2
        self.y = screen_size[1] / 2 - self.height / 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.default_velocity = 3
        self.sprint_velocity = 5
        self.velocity = self.default_velocity
        self.visible = True

    def move(self, entities, dx, dy):
        if dx != 0:
            # self.move_single_axis(entities, dx, 0)
            self.move_others(entities, dx, 0)
        if dy != 0:
            # self.move_single_axis(entities, 0, dy)
            self.move_others(entities, 0, dy)

    def move_others(self, entities, dx, dy):
        for key in entities:
            for item in entities[key]:
                item.rect.x += -dx
                item.rect.y += -dy

    def move_single_axis(self, entities, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        for obstacle in entities['obstacles']:
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

    def change_color(self, colors):
        self.color = random.choice(colors)

    def pick_up_key(self, inventory, key):
        if self.rect.colliderect(key.rect) and key.visible is True:
            inventory.add_key()
            key.visible = False
            print(f'Keys: {inventory.keys}')

    def pick_up_health_potion(self, inventory, health_potion):
        if self.rect.colliderect(health_potion.rect) and health_potion.visible is True:
            inventory.add_health_potion()
            health_potion.visible = False
            print(f'Health Potions: {inventory.health_potions}')


class Inventory():
    def __init__(self):
        self.keys = 0
        self.keys_limit = 3
        self.health_potions = 0
        self.health_potions_limit = 2

    def add_key(self):
        if self.keys < self.keys_limit:
            self.keys += 1

    def add_health_potion(self):
        if self.health_potions < self.health_potions_limit:
            self.health_potions += 1

from model import data_manager, util
import random


class Player():
    def __init__(self, color):
        self.name = 'Nick'
        self.color = color
        self.x = 10
        self.y = 10
        self.width = 64
        self.height = 64
        self.default_velocity = 2
        self.sprint_velocity = 5
        self.velocity = self.default_velocity
        self.hitbox = util.Hitbox([self.x, self.x + self.width, self.y + self.height, self.x + self.width + self.height])

    def move_up(self):
        self.y -= self.velocity

    def move_down(self):
        self.y += self.velocity

    def move_left(self):
        self.x -= self.velocity

    def move_right(self):
        self.x += self.velocity

    def walk(self):
        self.velocity = self.default_velocity

    def sprint(self):
        self.velocity = self.sprint_velocity

    def change_color(self, colors):
        self.color = random.choice(colors)

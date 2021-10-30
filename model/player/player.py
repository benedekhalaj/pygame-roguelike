from model import data_manager, util


class Player():
    def __init__(self, color):
        self.name = 'Nick'
        self.color = color
        self.x = 10
        self.y = 10
        self.width = 64
        self.height = 64
        self.velocity = 10
        self.hitbox = util.Hitbox([self.x, self.x + self.width, self.y + self.height, self.x + self.width + self.height])

    def move_up(self):
        self.y -= self.velocity

    def move_down(self):
        self.y += self.velocity

    def move_left(self):
        self.x -= self.velocity

    def move_right(self):
        self.x += self.velocity

    def sprint(self):
        self.velocity = 20

    def walk(self):
        self.velocity = 10

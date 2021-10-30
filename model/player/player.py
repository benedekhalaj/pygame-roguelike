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
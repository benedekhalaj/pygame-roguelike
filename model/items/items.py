from model import data_manager, util


class Rectangle():
    def __init__(self, color, position):
        self.color = color
        self.x = position[0]
        self.y = position[1]
        self.width = position[2]
        self.height = position[3]

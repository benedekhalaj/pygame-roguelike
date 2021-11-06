import pygame


class Enemy():
    def __init__(self, position, color):
        self.position = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color
        self.texture = None
        self.texture_count = 0
        self.texture_count_limit = 60

        self.color = color[0]
        self.visible = True

        self.visible = True

    def update_texture_count(self):
        if type(self.texture) is list:
            if self.texture_count + 1 >= self.texture_count_limit:
                self.texture_count = 0

            self.texture_count += 1
            print('updated')


class Zombie(Enemy):
    def __init__(self, position, color):
        super().__init__(position, color)


zombie = Zombie((0, 0, 0, 0), (0, 0, 0))

zombie.update_texture_count()

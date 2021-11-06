from model import data_manager
import pygame


pygame.mixer.init()
SFX_HIT_ENEMY = pygame.mixer.Sound('sound/sfx/hit_enemy.WAV')


class Zombie_Enemy():
    def __init__(self, position: tuple, file_path, colors: dict, direction):
        self.type = "standard"
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = None
        self.texture_count = 0
        self.texture_count_limit = 60
        self.color = colors.BROWN
        self.visible = True
        self.velocity = 4
        self.direction = direction[0]
        self.count_limit = direction[1]
        self.visible = True

    def move(self, objects):
        if self.direction == 'right':
            self.rect.x += self.velocity
        elif self.direction == 'left':
            self.rect.x -= self.velocity
        elif self.direction == 'down':
            self.rect.y += self.velocity
        elif self.direction == 'up':
            self.rect.y -= self.velocity

        for wall in objects['walls']:
            if self.rect.colliderect(wall.rect):
                if self.direction == 'right':
                    self.direction = 'left'
                elif self.direction == 'left':
                   self.direction = 'right'
                elif self.direction == 'down':
                    self.direction = 'up'
                elif self.direction == 'up':
                    self.direction = 'down'


    def take_damage(self, objects: dict):
        for player in objects["player"]:
            if player.sword.visible:
                if self.visible:
                    if self.rect.colliderect(player.sword.rect):
                        self.visible = False
                        SFX_HIT_ENEMY.play()

    def update_texture(self):
        path = 'model/map/textures/enemy/'
        if self.direction == 'left' or self.direction == 'up':
            self.texture = [data_manager.open_image(path, 'zombie/zombie_left.png'),
                            data_manager.open_image(path, 'zombie/zombie_left2.png')]
        elif self.direction == 'right' or self.direction == 'down':
            self.texture = [data_manager.open_image(path, 'zombie/zombie_right.png'),
                            data_manager.open_image(path, 'zombie/zombie_right2.png')]
        self.update_texture_count()

    def update_texture_count(self):
        if type(self.texture) is list:
            if self.texture_count + 1 >= self.texture_count_limit:
                self.texture_count = 0

            self.texture_count += 1


class Eye_Enemy():
    def __init__(self, position, file_path, colors):
        self.type = 'eye'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = create_texture(file_path)
        self.texture_count = 0
        self.texture_count_limit = 60
        self.color = colors.BROWN
        self.visible = True

    def set_facing(self, objects):
        player = objects['player'][0]
        path = 'model/map/textures/enemy/eyeball/'
        left = 'eyeball_left_'
        right = 'eyeball_right_'

        if player.rect.x > self.rect.x:
            if player.rect.y > self.rect.y + self.rect.height:
                self.texture = data_manager.open_image(path, f'{right}down.png')
            elif player.rect.y > self.rect.y:
                self.texture = data_manager.open_image(path, f'{right}middle.png')
            else:
                self.texture = data_manager.open_image(path, f'{right}up.png')
        else:
            if player.rect.y > self.rect.y + self.rect.height:
                self.texture = data_manager.open_image(path, f'{left}down.png')
            elif player.rect.y > self.rect.y:
                self.texture = data_manager.open_image(path, f'{left}middle.png')
            else:
                self.texture = data_manager.open_image(path, f'{left}up.png')


def create_texture(file_path):
    if file_path is not None:
        return pygame.image.load(file_path)
    else:
        return None

from model import data_manager
import pygame


pygame.mixer.init()
SFX_HIT_ENEMY = pygame.mixer.Sound('sound/sfx/hit_enemy.WAV')


class Zombie_Enemy():
    def __init__(self, position: tuple, file_path, colors: dict, direction):
        self.type = "standard"
        self.rect = pygame.Rect(position[0], position[1], position[2] - 10, position[3] - 5)
        self.texture = None
        self.texture_count = 0
        self.texture_count_limit = 60
        self.color = colors.BROWN

        self.velocity = 2
        self.direction = direction[0]
        self.count_limit = direction[1]

        self.health = 2
        self.damage_timer = 0
        self.damage_limit = 30
        self.invicible = False

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
        self.set_damage_attributes()
        for player in objects["player"]:
            if self.visible and player.sword.visible:
                if self.rect.colliderect(player.sword.rect):
                    if not self.invicible:
                        self.health -= 1
                        self.invicible = True
                        SFX_HIT_ENEMY.play()
        self.vanish()

    def set_damage_attributes(self):
        def set_invicible(self):
            if self.damage_timer > self.damage_limit:
                self.invicible = False

        def set_damage_timer(self):
            if self.invicible:
                self.damage_timer += 1
            else:
                self.damage_timer = 0

        set_invicible(self)
        set_damage_timer(self)

    def vanish(self):
        if self.health < 1:
            self.visible = False



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


class Shooter_Enemy():
    def __init__(self, position, file_path, colors):
        self.type = 'shooter'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = create_texture(None)
        self.texture_count = 0
        self.texture_count_limit = 60
        self.color = colors.BROWN
        self.visible = True


def create_texture(file_path):
    if file_path is not None:
        return pygame.image.load(file_path)
    else:
        return None

from model import data_manager
import pygame
import random


pygame.mixer.init()

SFX_HIT_ZOMBIE_1 = data_manager.open_sfx('sound/sfx/zombie/hit_zombie1.ogg')
SFX_HIT_ZOMBIE_2 = data_manager.open_sfx('sound/sfx/zombie/hit_zombie2.ogg')
SFX_HIT_ZOMBIE_3 = data_manager.open_sfx('sound/sfx/zombie/hit_zombie3.ogg')


class Zombie_Enemy():
    def __init__(self, texture_id, position: tuple, file_path, colors: dict, direction):
        self.type = "standard"
        self.rect = pygame.Rect(position[0], position[1], position[2] - 14, position[3] - 5)
        self.texture = None
        self.texture_id = texture_id
        self.texture_count = 0
        self.texture_count_limit = 60
        self.color = colors.BROWN

        self.velocity = 2
        self.direction = direction[0]
        self.count_limit = direction[1]

        self.max_health = 2
        self.health = 2
        self.health_bar = Health_Bar((self.rect.x, self.rect.y, self.rect.width, self.rect.height), (colors.BLACK, colors.LIGHT_YELLOW))

        self.damage_timer = 0
        self.damage_limit = 30
        self.invicible = False

        self.created_brain = False
        self.visible = True

        self.growl_count = 0
        self.growl_count_limit = random.randint(100, 400)

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
                        self.decrease_health_bar()
                        zombie_hit_sounds = [SFX_HIT_ZOMBIE_1, SFX_HIT_ZOMBIE_2, SFX_HIT_ZOMBIE_3]
                        random.choice(zombie_hit_sounds).play()
        self.vanish(objects)

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

    def vanish(self, objects):
        if self.health < 1:
            self.visible = False
            if not self.created_brain:
                self.create_brain(objects)
                self.created_brain = True

    def create_brain(self, objects):
        objects['items'].append(Brain((self.rect.x, self.rect.y, 32, 32)))

    def update_hitbox(self):
        if self.direction == 'up' or self.direction == 'down':
            self.rect.width = 30
        else:
            self.rect.width = 50

    def update_health_bar(self):
        self.health_bar.rect.x = self.rect.x + self.health_bar.border
        self.health_bar.rect.y = self.rect.y - self.health_bar.y_offset + self.health_bar.border
        self.health_bar.background.x = self.rect.x
        self.health_bar.background.y = self.rect.y - self.health_bar.y_offset

    def decrease_health_bar(self):
        unit = self.health_bar.width / self.max_health
        self.health_bar.rect.width -= unit

        if self.health < 1:
            self.health_bar.visible = False

    def update_texture(self):
        path = 'model/map/textures/enemy/'
        if self.direction == 'left':
            self.texture = [data_manager.open_image(path, 'zombie/zombie_left.png'),
                            data_manager.open_image(path, 'zombie/zombie_left2.png')]
        elif self.direction == 'right':
            self.texture = [data_manager.open_image(path, 'zombie/zombie_right.png'),
                            data_manager.open_image(path, 'zombie/zombie_right2.png')]
        elif self.direction == 'down':
            self.texture = [data_manager.open_image(path, 'zombie/zombie_down.png'),
                            data_manager.open_image(path, 'zombie/zombie_down2.png')]
        elif self.direction == 'up':
            self.texture = [data_manager.open_image(path, 'zombie/zombie_up.png'),
                            data_manager.open_image(path, 'zombie/zombie_up2.png')]
        self.update_texture_count()

    def update_texture_count(self):
        if type(self.texture) is list:
            if self.texture_count + 1 >= self.texture_count_limit:
                self.texture_count = 0

            self.texture_count += 1

    def update_brain_texture(self, objects):
        for item in objects['items']:
            if item.type == 'brain':
                item.update_texture_count()


class Brain():
    def __init__(self, position):
        self.type = 'brain'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = [data_manager.open_image('model/map/textures/items/brain/brain1.png'),
                        data_manager.open_image('model/map/textures/items/brain/brain2.png')]
        self.texture_count = 0
        self.texture_count_limit = 60
        self.color = (166, 32, 100)

        self.visible = True

    def update_texture_count(self):
        if type(self.texture) is list:
            if self.texture_count + 1 >= self.texture_count_limit:
                self.texture_count = 0

            self.texture_count += 1


class Eye_Enemy():
    def __init__(self, texture_id, position, file_path, colors):
        self.type = 'eye'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = create_texture(file_path)
        self.texture_id = texture_id
        self.texture_count = 0
        self.texture_count_limit = 60
        self.color = colors.BROWN
        self.visible = True

        self.health = 1
        self.damage_timer = 0
        self.damage_limit = 30
        self.invicible = False

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

    def take_damage(self, objects: dict):
        self.set_damage_attributes()
        for player in objects["player"]:
            if self.visible and player.sword.visible:
                if self.rect.colliderect(player.sword.rect):
                    if not self.invicible:
                        self.health -= 1
                        self.invicible = True
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



class Shooter_Enemy():
    def __init__(self, texture_id, position, file_path, colors, direction):
        self.type = 'shooter'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = create_texture(file_path)
        self.texture_id = texture_id
        self.texture_count = 0
        self.texture_count_limit = 60
        self.color = colors.BROWN

        self.health = 3
        self.damage_timer = 0
        self.damage_limit = 30
        self.invicible = False

        self.velocity = 5
        self.move_direction = direction[0]
        self.shoot_direction = direction[1]

        self.projectiles = []
        self.projectile_timer = 0
        self.projectile_timer_limit = 60
        self.projectile_width = 32
        self.projectile_height = 32

        self.visible = True

    def move(self, objects):
        if self.move_direction == 'right':
            self.rect.x += self.velocity
        elif self.move_direction == 'left':
            self.rect.x -= self.velocity
        elif self.move_direction == 'down':
            self.rect.y += self.velocity
        elif self.move_direction == 'up':
            self.rect.y -= self.velocity

        for wall in objects['walls']:
            if self.rect.colliderect(wall.rect):
                if self.move_direction == 'right':
                    self.move_direction = 'left'
                elif self.move_direction == 'left':
                    self.move_direction = 'right'
                elif self.move_direction == 'down':
                    self.move_direction = 'up'
                elif self.move_direction == 'up':
                    self.move_direction = 'down'

    def shoot(self, objects):
        if self.visible:
            self.update_projectile_timer()

            if self.projectile_timer > self.projectile_timer_limit:
                self.set_projectile_position()

                self.projectile_timer = 0
        self.move_projectile(objects)

    def set_projectile_position(self):
        if self.shoot_direction == 'right':
            projectile_position = (self.rect.x + self.rect.width, self.rect.y + self.rect.height / 4, 32, 32)
        elif self.shoot_direction == 'left':
            projectile_position = (self.rect.x - self.rect.width, self.rect.y + self.rect.height / 4, 32, 32)
        elif self.shoot_direction == 'down':
            projectile_position = (self.rect.x + self.rect.width / 4, self.rect.y + self.rect.height, 32, 32)
        elif self.shoot_direction == 'up':
            projectile_position = (self.rect.x + self.rect.width / 4, self.rect.y - self.rect.height, 32, 32)
        self.projectiles.append(Projectile(projectile_position, self.shoot_direction))

    def update_projectile_timer(self):
        self.projectile_timer += 1

    def move_projectile(self, objects):
        for projectile in self.projectiles:
            if projectile.direction == 'left':
                projectile.rect.x -= projectile.velocity
            elif projectile.direction == 'right':
                projectile.rect.x += projectile.velocity
            elif projectile.direction == 'up':
                projectile.rect.y -= projectile.velocity
            elif projectile.direction == 'down':
                projectile.rect.y += projectile.velocity
        self.collide_projectile(objects)

    def collide_projectile(self, objects):
        for projectile in self.projectiles:
            for wall in objects['walls']:
                if projectile.rect.colliderect(wall.rect):
                    projectile.visible = False
            sword = objects['player'][0].sword
            if projectile.hitable:
                if sword.visible and sword.projectile_knockback:
                    if projectile.rect.colliderect(sword.rect):
                        projectile.direction = sword.direction
                        projectile.hitable = False
            projectile.check_if_hitable()
            if self.rect.colliderect(projectile.rect):
                self.visible = False
                projectile.visible = False

    def delete_projectile(self):
        for projectile in self.projectiles:
            if not projectile.visible:
                self.projectiles.pop(self.projectiles.index(projectile))
                break

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


class Projectile():
    def __init__(self, position, direction):
        self.type = 'projectile'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = (244, 140, 86)
        self.texture = None

        self.velocity = 5
        self.direction = direction

        self.hitable = True
        self.hit_timer = 0
        self.hit_timer_limit = 30

        self.visible = True

    def check_if_hitable(self):
        if not self.hitable:
            self.update_hit_timer()

    def update_hit_timer(self):
        self.hit_timer += 1

        if self.hit_timer > self.hit_timer_limit:
            self.hit_timer = 0
            self.hitable = True


def create_texture(file_path):
    if file_path is not None:
        return pygame.image.load(file_path)
    else:
        return None


class Health_Bar():
    def __init__(self, position, colors):
        self.type = 'health_bar'

        self.x = position[0]
        self.y_offset = 20
        self.y = position[1] - self.y_offset
        self.width = position[2]
        self.height = 16

        self.background = pygame.Rect(self.x, self.y, self.width, self.height)
        self.background_color = colors[0]

        self.border = 2
        self.rect = pygame.Rect(self.x + self.border, self.y + self.border, self.width - 4, self.height - 4)

        self.color = colors[1]

        self.texture = None

        self.visible = True

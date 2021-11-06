from model import data_manager
import pygame
import pygame.freetype

from model.map.map import create_map_sign_dict


pygame.mixer.init()
SFX_PICK_UP_KEY = data_manager.open_sfx('sound/sfx/pick_up_key.WAV')
SFX_OPEN_DOOR = data_manager.open_sfx('sound/sfx/open_door.WAV')
SFX_PICK_UP_SWORD = data_manager.open_sfx('sound/sfx/pick_up_sword.WAV')


class Player():
    def __init__(self, position: tuple, file_path, colors, screen_size):
        self.type = 'player'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.texture = data_manager.open_image(file_path)
        self.texture_count = 0
        self.texture_count_limit = 60

        self.colors = colors
        self.standard_color = colors.RED
        self.invicible_color = colors.ORANGE
        self.color = self.standard_color

        self.walk_speed = 4
        self.stamina_limit = 60
        self.spirnt_multiplier = 2
        self.sprint_speed = self.walk_speed * self.spirnt_multiplier
        self.velocity = self.walk_speed
        self.sprinting = False
        self.can_spirnt = True
        self.stamina = 1  # self.stamina_limit

        self.moving = True
        self.direction = 'right'

        self.damage_timer = 0
        self.damage_limit = 120
        self.invicible = False

        self.inventory = Inventory()
        self.attack_in_progress = False
        self.attack_timer_count = 0
        self.attack_timer_limit = 30
        self.attack_duration = 12
        self.sword = Sword((self.rect.x + self.rect.width, self.rect.y, self.rect.width, self.rect.height), colors, self.attack_duration)

        self.max_health = 5
        self.health = 1
        self.stat = Stat(colors, screen_size, (self.health, self.max_health, self.stamina, self.stamina_limit))
        self.visible = True

    def move(self, objects, x_direction, y_direction):
        if x_direction != 0:
            self.move_single_axis(objects, x_direction, 0)
        if y_direction != 0:
            self.move_single_axis(objects, 0, y_direction)

    def set_direction(self, x_direction, y_direction):
        if x_direction > 0:
            self.direction = 'right'
        if x_direction < 0:
            self.direction = 'left'
        if y_direction > 0:
            self.direction = 'down'
        if y_direction < 0:
            self.direction = 'up'

    def sprint(self):
        if self.stamina > 0 and self.can_spirnt:
            self.sprinting = True
            self.velocity = self.sprint_speed
            self.stamina -= 1
        else:
            self.can_spirnt = False
            self.sprinting = False
            self.velocity = self.walk_speed

    def reload_stamina(self):
        if self.stamina < self.stamina_limit:
            self.stamina += 0.5
            self.velocity = self.walk_speed
        if self.stamina >= self.stamina_limit:
            self.can_spirnt = True

    def check_collision(self, objects):
        if self.check_wall_collision(objects) or self.check_door_collision(objects):
            return True
        else:
            return False

    def check_wall_collision(self, objects):
        for wall in objects["walls"]:
            if self.rect.colliderect(wall.rect):
                self.set_collision_direction(wall)
                return True
        return False

    def check_door_collision(self, objects):
        self.open_door(objects)
        for door in objects["doors"]:
            if self.rect.colliderect(door.rect):
                if door.status == "closed":
                    self.set_collision_direction(door)
                    return True
        return False

    def set_collision_direction(self, object):
        if self.direction == 'right':
            self.rect.right = object.rect.left
        elif self.direction == 'left':
            self.rect.left = object.rect.right
        elif self.direction == 'down':
            self.rect.bottom = object.rect.top
        elif self.direction == 'up':
            self.rect.top = object.rect.bottom

    def move_single_axis(self, objects: dict, x_direction, y_direction):
        self.set_direction(x_direction, y_direction)

        self.rect.x += x_direction
        self.rect.y += y_direction

        collide = self.check_collision(objects)

        if not collide:
            for objects_list in objects.values():
                for item in objects_list:
                    item.rect.x -= x_direction
                    item.rect.y -= y_direction

    def add_item_to_inventory(self, objects: dict):
        for item in objects["items"]:
            if self.rect.colliderect(item.rect):
                if item.visible:
                    if item.type == 'key':
                        self.inventory.add_key()
                        item.visible = False
                        SFX_PICK_UP_KEY.play()
                    elif item.type == 'health_potion':
                        self.inventory.add_health_potion()
                        item.visible = False
                    elif item.type == 'sword':
                        self.sword.exist = True
                        item.visible = False
                        SFX_PICK_UP_SWORD.play()

    def use_inventory(self, objects, pause, key):
        self.show_inventory()
        if key[pygame.K_ESCAPE]:
            pause = False
        else:
            pause = True
        return pause

    def show_inventory(self):
        print("Hello")
        pass

    def open_door(self, objects):
        for door in objects["doors"]:
            if self.rect.colliderect(door.rect):
                if self.inventory.keys > 0:
                    if door.status == "closed":
                        door.status = "opened"
                        door.update_color()
                        self.inventory.remove_key()
                        SFX_OPEN_DOOR.play()

    def take_damage(self, objects: dict):
        self.set_attributes()
        for enemy in objects["enemies"]:
            if enemy.visible:
                if self.rect.colliderect(enemy.rect):
                    if not self.invicible:
                        self.health -= 1
                        self.invicible = True

    def set_attributes(self):
        def set_invicible(self):
            if self.damage_timer > self.damage_limit:
                self.invicible = False

        def set_damage_timer(self):
            if self.invicible:
                self.damage_timer += 1
            else:
                self.damage_timer = 0

        def set_color(self):
            if self.invicible:
                self.color = self.invicible_color
            else:
                self.color = self.standard_color

        def update_stat(self):
            self.stat.texts = self.stat.create_stat_text((self.health, self.max_health, self.stamina, self.stamina_limit))
            self.stat.bars = self.stat.create_stat_bar((self.health, self.max_health, self.stamina, self.stamina_limit))

        set_invicible(self)
        set_damage_timer(self)
        set_color(self)
        update_stat(self)

    def set_sword_position(self):
        player = self.rect
        sword = self.sword.rect
        if self.direction == 'right':
            sword.x = player.x + player.width
            sword.y = player.y

        elif self.direction == 'left':
            sword.x = player.x - player.width
            sword.y = player.y

        elif self.direction == 'down':
            sword.x = player.x
            sword.y = player.y + player.height

        elif self.direction == 'up':
            sword.x = player.x
            sword.y = player.y - player.height

    def attack(self):
        if self.attack_in_progress:
            self.sword.visible = True
            self.update_attack_timer()
            self.check_attack_timer()
            self.sword.update_texture()

    def update_attack_timer(self):
        self.attack_timer_count += 1

    def check_attack_timer(self):
        if self.attack_timer_count > self.attack_duration:
            self.sword.visible = False
        if self.attack_timer_count > self.attack_timer_limit:
            self.attack_timer_count = 0
            self.attack_in_progress = False

    def update_texture(self):
        if self.moving:
            path = 'model/map/textures/player/'
            left = 'knight_left'
            right = 'knight_right'
            up = 'knight_up'
            down = 'knight_down'
            if self.direction == 'left':
                self.texture = [data_manager.open_image(path, f'{left}1.png'),
                                data_manager.open_image(path, f'{left}2.png'),
                                data_manager.open_image(path, f'{left}3.png'),
                                data_manager.open_image(path, f'{left}2.png')]
            elif self.direction == 'right':
                self.texture = [data_manager.open_image(path, f'{right}1.png'),
                                data_manager.open_image(path, f'{right}2.png'),
                                data_manager.open_image(path, f'{right}3.png'),
                                data_manager.open_image(path, f'{right}2.png')]
            elif self.direction == 'up':
                self.texture = [data_manager.open_image(path, f'{up}1.png'),
                                data_manager.open_image(path, f'{up}2.png'),
                                data_manager.open_image(path, f'{up}3.png'),
                                data_manager.open_image(path, f'{up}2.png')]
            elif self.direction == 'down':
                self.texture = [data_manager.open_image(path, f'{down}1.png'),
                                data_manager.open_image(path, f'{down}2.png'),
                                data_manager.open_image(path, f'{down}3.png'),
                                data_manager.open_image(path, f'{down}2.png')]
            self.update_texture_count()

    def update_texture_count(self):
        if self.texture_count + 1 >= self.texture_count_limit:
            self.texture_count = 0

        self.texture_count += 1


class Inventory():
    def __init__(self):
        self.keys = 0
        self.keys_limit = 99
        self.health_potions = 0
        self.health_potions_limit = 1

    def add_key(self):
        if self.keys < self.keys_limit:
            self.keys += 1

    def remove_key(self):
        self.keys -= 1

    def add_health_potion(self):
        if self.health_potions < self.health_potions_limit:
            self.health_potions += 1

    def use_inventory(self):
        pass

class Sword():
    def __init__(self, position: tuple, colors: object, attack_duration):
        self.exist = False

        self.texture = None
        self.texture_count = 0
        self.texture_count_limit = attack_duration

        self.color = colors.PURPLE
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.visible = False
        self.direction = 'left'

    def update_texture(self):
        path = 'model/map/textures/player/'
        left = 'stab_fx_left'
        right = 'stab_fx_right'
        up = 'stab_fx_up'
        down = 'stab_fx_down'
        if self.direction == 'left':
            self.texture = [data_manager.open_image(path, f'{left}1.png'),
                            data_manager.open_image(path, f'{left}2.png'),
                            data_manager.open_image(path, f'{left}3.png'),
                            data_manager.open_image(path, f'{left}3.png')]

        elif self.direction == 'right':
            self.texture = [data_manager.open_image(path, f'{right}1.png'),
                            data_manager.open_image(path, f'{right}2.png'),
                            data_manager.open_image(path, f'{right}3.png')]

        elif self.direction == 'up':
            self.texture = [data_manager.open_image(path, f'{up}1.png'),
                            data_manager.open_image(path, f'{up}2.png'),
                            data_manager.open_image(path, f'{up}3.png')]

        elif self.direction == 'down':
            self.texture = [data_manager.open_image(path, f'{down}1.png'),
                            data_manager.open_image(path, f'{down}2.png'),
                            data_manager.open_image(path, f'{down}3.png')]

        self.update_texture_count()

    def update_texture_count(self):
        if self.texture_count + 1 >= self.texture_count_limit:
            self.texture_count = 0

        self.texture_count += 1



class Stat():
    def __init__(self, colors, screen_size, player_stats):
        self.type = "stat"
        self.x = 1
        self.y = 1
        self.width = screen_size[0] // 5
        self.height = screen_size[1] // 60
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = colors
        self.health = "health"
        self.stamina = 'stamina'
        self.visible = True
        self.font_size = 20
        self.texts = self.create_stat_text(player_stats)
        self.bars = self.create_stat_bar(player_stats)

    def create_stat_bar(self, player_stat):
        number = 0
        bar = []
        
        player_health = player_stat[0]
        player_max_health = player_stat[1]
        player_stamina = player_stat[2]
        player_max_stamina = player_stat[3]
        for type, text in self.texts.items():
            y = self.y + number * self.font_size
            x = self.x + (text.get_width()) + 8
            if type == self.health:
                width = self.width * (player_health / player_max_health)
                color = self.color.RED
                stamina_texture = create_stat_bar_texture(self.width, self.height, x, y)
            elif type == self.stamina:
                width = self.width * (player_stamina / player_max_stamina)
                color = self.color.BLUE
                stamina_texture = create_stat_bar_texture(self.width, self.height, x, y)
            number += 1
            bar.append([(pygame.Rect(x, y, width, self.height), color), stamina_texture])
        return bar

    def create_stat_text(self, player_stats):
        texts = {}
        font_type = 'couriernew'
        player_health = player_stats[0]
        player_stamina = player_stats[2]
        font = pygame.font.SysFont(font_type, self.font_size, bold=True)
        texts[self.health] = font.render(f"{player_health} hp", False, self.color.WHITE)
        texts[self.stamina] = font.render(f"{int(player_stamina)} stamina", False, self.color.WHITE)
        return texts
        # pygame.font.get_fonts()


def create_stat_bar_texture(width, height, x, y):
    x = x
    self_height = height
    stat_bar_start = pygame.image.load("model/map/textures/misc/stat_bar_start.png")
    stat_bar_start = pygame.transform.scale(stat_bar_start, (32, self_height))
    stat_bar_start_width = stat_bar_start.get_width()
    stat_bar_middle = pygame.image.load("model/map/textures/misc/stat_bar_middle.png")
    stat_bar_middle = pygame.transform.scale(stat_bar_middle, (32, self_height))
    stat_bar_middle_width = stat_bar_middle.get_width()
    stat_bar_end = pygame.image.load("model/map/textures/misc/stat_bar_end.png")
    stat_bar_end = pygame.transform.scale(stat_bar_end, (32, self_height))
    stat_bar_end_width = stat_bar_end.get_width()
    lenght_of_stat_bar = int((width - stat_bar_start_width - stat_bar_end_width) / stat_bar_middle_width)
    bar_texture = [(stat_bar_start, x, y)]
    for _ in range(lenght_of_stat_bar):
        x += stat_bar_middle_width
        bar_texture.append((stat_bar_middle, x, y))
    bar_texture.append((stat_bar_end, x + stat_bar_end_width, y))
    return bar_texture



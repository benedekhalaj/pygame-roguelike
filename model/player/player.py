from pygame.constants import SCRAP_SELECTION
from model import data_manager
import pygame
import pygame.freetype


class Player():
    def __init__(self, position: tuple, colors, screen_size):
        self.type = 'player'
        self.texture = None
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])

        self.colors = colors
        self.standard_color = colors.RED
        self.invicible_color = colors.ORANGE
        self.color = self.standard_color

        self.walk_speed = 8
        self.sprint_speed = self.walk_speed * 3
        self.velocity = self.walk_speed
        self.sprinting = False
        self.can_spirnt = True
        self.stamina_limit = 60

        self.direction = 'right'

        self.damage_timer = 0
        self.damage_limit = 120
        self.invicible = False

        self.inventory = Inventory()
        self.sword = Sword((self.rect.x + self.rect.width, self.rect.y, self.rect.width, self.rect.height), colors.PURPLE)
        self.attack_in_progress = False
        self.attack_timer_count = 0
        self.attack_timer_limit = 60
        self.attack_duration = 40

        self.health = 1
        self.stamina = self.stamina_limit
        self.stat = Stat(colors, screen_size, self.health)
        self.visible = True

    def move(self, objects, x_direction, y_direction):
        if x_direction != 0:
            self.move_single_axis(objects, x_direction, 0)
        if y_direction != 0:
            self.move_single_axis(objects, 0, y_direction)
        if not self.sprinting:
            self.reload_stamina()

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
                    elif item.type == 'health_potion':
                        self.inventory.add_health_potion()
                        item.visible = False
                    elif item.type == 'sword':
                        self.sword.exist = True
                        item.visible = False

    def open_door(self, objects):
        for door in objects["doors"]:
            if self.rect.colliderect(door.rect):
                if self.inventory.keys > 0:
                    if door.status == "closed":
                        door.status = "opened"
                        door.update_color()
                        self.inventory.remove_key()

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
            self.stat.text = self.stat.create_text(self.colors, self.health)

        set_invicible(self)
        set_damage_timer(self)
        set_color(self)
        update_stat(self)

    def set_sword_position(self):
        if self.direction == 'right':
            self.sword.rect.x = self.rect.x + self.rect.width
            self.sword.rect.y = self.rect.y
        elif self.direction == 'left':
            self.sword.rect.x = self.rect.x - self.rect.width
            self.sword.rect.y = self.rect.y
        elif self.direction == 'down':
            self.sword.rect.x = self.rect.x
            self.sword.rect.y = self.rect.y + self.rect.height
        elif self.direction == 'up':
            self.sword.rect.x = self.rect.x
            self.sword.rect.y = self.rect.y - self.rect.height

    def attack(self):
        if self.attack_in_progress:
            self.sword.visible = True
            self.update_attack_timer()
            self.check_attack_timer()

    def update_attack_timer(self):
        self.attack_timer_count += 1

    def check_attack_timer(self):
        if self.attack_timer_count > self.attack_duration:
            self.sword.visible = False
        if self.attack_timer_count > self.attack_timer_limit:
            self.attack_timer_count = 0
            self.attack_in_progress = False


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


class Sword():
    def __init__(self, position: tuple, color: tuple):
        self.exist = False
        self.color = color
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.visible = False


class Stat():
    def __init__(self, colors, screen_size, player_health):
        self.type = "stat"
        self.x = 0
        self.y = 0
        self.width = screen_size[0] // 5
        self.height = screen_size[1] // 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = colors.BROWN
        self.visible = True
        self.text = self.create_text(colors, player_health)

    def create_text(self, colors, player_health):
        font_type = 'couriernew'
        font_size = 30
        font = pygame.font.SysFont(font_type, font_size, bold=True)
        textsurface = font.render(f"{player_health} hp", False, colors.WHITE)
        return textsurface
        # pygame.font.get_fonts()

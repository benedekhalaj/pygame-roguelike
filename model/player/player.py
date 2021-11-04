from model import data_manager
import pygame
import pygame.freetype


class Player():
    def __init__(self, position: tuple, colors, screen_size):
        self.type = 'player'
        self.texture = None
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.standard_color = colors.RED
        self.invicible_color = colors.ORANGE
        self.colors = colors
        self.color = self.standard_color
        self.velocity = 4
        self.health = 100
        self.inventory = Inventory()
        self.visible = True
        self.damage_timer = 0
        self.damage_limit = 120
        self.invicible = False
        self.sword = Sword((self.rect.x + self.rect.width, self.rect.y, self.rect.width, self.rect.height), colors.PURPLE)
        self.stat = Stat(colors, screen_size, self.health)

    def move(self, objects, x_direction, y_direction):
        if x_direction != 0:
            self.move_single_axis(objects, x_direction, 0)
        if y_direction != 0:
            self.move_single_axis(objects, 0, y_direction)

    def move_single_axis(self, objects: dict, x_direction, y_direction):
        collide = False
        self.rect.x += x_direction
        self.rect.y += y_direction

        for item in objects["walls"]:
            if self.rect.colliderect(item.rect):
                if x_direction > 0:
                    self.rect.right = item.rect.left
                if x_direction < 0:
                    self.rect.left = item.rect.right
                if y_direction > 0:
                    self.rect.bottom = item.rect.top
                if y_direction < 0:
                    self.rect.top = item.rect.bottom
                collide = True
        if not collide:
            for objects_list in objects.values():
                for item in objects_list:
                    item.rect.x -= x_direction
                    item.rect.y -= y_direction

    def add_item_to_inventory(self, objects: dict):
        for item in objects["items"]:
            if self.rect.colliderect(item.rect):
                if item.type == 'key':
                    self.inventory.add_key()
                    item.visible = False
                elif item.type == 'health_potion':
                    self.inventory.add_health_potion()
                    item.visible = False

    def take_damage(self, objects: dict):
        self.set_attributes()
        for object in objects["enemies"]:
            if self.rect.colliderect(object.rect):
                if not self.invicible:
                    self.health -= 1
                    self.invicible = True

    def set_attributes(self):
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

        def set_invicible(self):
            if self.damage_timer > self.damage_limit:
                self.invicible = False

        def update_stat(self):
            self.stat.text = self.stat.create_text(self.colors, self.health)

        set_damage_timer(self)
        set_color(self)
        set_invicible(self)
        update_stat(self)


class Inventory():
    def __init__(self):
        self.keys = 0
        self.keys_limit = 99
        self.health_potions = 0
        self.health_potions_limit = 1

    def add_key(self):
        if self.keys < self.keys_limit:
            self.keys += 1

    def add_health_potion(self):
        if self.health_potions < self.health_potions_limit:
            self.health_potions += 1


class Sword():
    def __init__(self, position: tuple, color: tuple):
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

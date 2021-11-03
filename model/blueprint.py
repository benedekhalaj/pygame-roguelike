import pygame


class Player():
    def __init__(self, position: tuple, color):
        self.type = 'player'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.standard_color = color[0]
        self.invicible_color = color[1]
        self.color = self.standard_color
        self.velocity = 4
        self.inventory = Inventory()
        self.visible = True
        self.damage_timer = 0
        self.damage_limit = 120
        self.invicible = False

    def move(self, objects, x_direction, y_direction):
        if x_direction != 0:
            self.move_single_axis(objects, x_direction, 0)
        if y_direction != 0:
            self.move_single_axis(objects, 0, y_direction)

    def move_single_axis(self, objects, x_direction, y_direction):
        collide = False
        self.rect.x += x_direction
        self.rect.y += y_direction

        for item in objects:
            if item.type == 'wall':
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
            for item in objects:
                item.rect.x -= x_direction
                item.rect.y -= y_direction


    def add_item_to_inventory(self, objects):
        for item in objects:
            if self.rect.colliderect(item.rect):
                if item.type == 'key':
                    self.inventory.add_key()
                    item.visible = False
                elif item.type == 'health_potion':
                    self.inventory.add_health_potion()
                    item.visible = False

    def take_damage(self,objects):
        self.start_damage_timer()
        for object in objects:
            if object.type == "enemy":
                if self.rect.colliderect(object.rect):
                    if self.damage_timer < 1:
                        print("hello")
                        self.invicible = True
                    

    def start_damage_timer(self):
        if self.invicible:
            self.damage_timer += 1
            self.color = self.invicible_color
        if self.damage_timer > self.damage_limit:
            self.invicible = False
            self.damage_timer = 0
            self.color = self.standard_color


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


class Key():
    def __init__(self, position, color):
        self.type = 'key'
        self.color = color
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.visible = True


class Health_Potion():
    def __init__(self, position, color):
        self.type = 'health_potion'
        self.color = color
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.visible = True


class Wall():
    def __init__(self, position, color):
        self.type = 'wall'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color
        self.visible = True


class Chest():
    def __init__(self, position, color):
        self.type = 'chest'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color
        self.visible = True


class Floor():
    def __init__(self, position, color):
        self.type = 'floor'
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color
        self.visible = True

class Enemy():
    def __init__(self, position, color):
        self.type = "enemy"
        self.rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.color = color
        self.visible = True
        self.velocity = 14
        self.count = 0
        self.count_direction = 60
        self.count_limit = self.count_direction * 2

    def move(self):
        if self.count <= self.count_direction:
            self.rect.x += self.velocity
        elif self.count > self.count_direction:
            self.rect.x -= self.velocity
        if self.count > self.count_limit:
            self.count = 0
        else:
            self.count += 1


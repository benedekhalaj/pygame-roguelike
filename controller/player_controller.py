from model.player import player
from view import terminal as view
import pygame


def get_colors():
    return [view.RED, view.BLUE, view.GREEN, view.YELLOW]


def get_player():
    return player.Player(view.RED)


def get_inventory():
    return player.Inventory()


def control_player(player, obstacles):
    keys = view.get_input()

    if keys[pygame.K_LEFT]:
        player.move(obstacles, -player.velocity, 0)
    if keys[pygame.K_RIGHT]:
        player.move(obstacles, player.velocity, 0)
    if keys[pygame.K_UP]:
        player.move(obstacles, 0, -player.velocity)
    if keys[pygame.K_DOWN]:
        player.move(obstacles, 0, player.velocity)
    if keys[pygame.K_LSHIFT]:
        player.sprint()
    else:
        player.walk()


def add_items_to_inventory(player, items, inventory):
    for item in items:
        if item.type == 'key':
            player.pick_up_key(inventory, item)
        elif item.type == 'potion':
            if item.sub_type == 'health':
                player.pick_up_health_potion(inventory, item)

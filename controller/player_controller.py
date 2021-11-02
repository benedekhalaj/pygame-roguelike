from model.player import player
from view import terminal as view
import pygame


def get_colors():
    return [view.RED, view.BLUE, view.GREEN, view.YELLOW]


def get_player():
    return player.Player(view.RED, (view.SCREEN_WIDTH, view.SCREEN_HEIGHT))


def get_inventory():
    return player.Inventory()


def control_player(player, entities, current_time):
    keys = view.get_input()

    if keys[pygame.K_LEFT]:
        player.move(entities, -player.velocity, 0)
    if keys[pygame.K_RIGHT]:
        player.move(entities, player.velocity, 0)
    if keys[pygame.K_UP]:
        player.move(entities, 0, -player.velocity)
    if keys[pygame.K_DOWN]:
        player.move(entities, 0, player.velocity)
    if keys[pygame.K_LSHIFT]:
        player.sprint()
    else:
        player.walk()
    if keys[pygame.K_SPACE]:
        key_pressed_time = pygame.time.get_ticks()
        if key_pressed_time + 2000 < current_time:
            colors = get_colors()
            player.change_color(colors)


def add_items_to_inventory(player, items, inventory):
    for item in items:
        if item.type == 'key':
            player.pick_up_key(inventory, item)
        elif item.type == 'potion':
            if item.sub_type == 'health':
                player.pick_up_health_potion(inventory, item)

from model.player import player
from view import view
import pygame


def change_player_on_input(player_character, objects):
    keys = view.get_input()

    if keys[pygame.K_LEFT]:
        player_character.move(objects, -player_character.velocity, 0)
    if keys[pygame.K_RIGHT]:
        player_character.move(objects, player_character.velocity, 0)
    if keys[pygame.K_UP]:
        player_character.move(objects, 0, -player_character.velocity)
    if keys[pygame.K_DOWN]:
        player_character.move(objects, 0, player_character.velocity)

    if keys[pygame.K_h]:
        if not player_character.currently_healing:
            player_character.heal_player()
            player_character.currently_healing = True
    else:
        player_character.currently_healing = False

    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        player_character.sprinting = True

    if keys[pygame.K_SPACE]:
        if player_character.sword.exist:
            if not player_character.attack_in_progress:
                player_character.start_attack()


def control_inventory(objects, pause):
    keys = view.get_input()
    inventory = objects['player'][0].inventory

    inventory.update_visible_timer()
    inventory.update_invisible_timer()

    if not pause and keys[pygame.K_i]:
        if inventory.can_show:
            inventory.show_inventory()
            pause = True
    elif pause and keys[pygame.K_i]:
        if inventory.can_hide:
            inventory.hide_inventory()
            pause = False
    return pause


def control_player(objects):
    player_character = objects['player'][0]

    player_character.moving = False
    change_player_on_input(player_character, objects)

    player_character.add_item_to_inventory(objects)
    player_character.update_stat()
    player_character.take_damage(objects)
    if player_character.sprinting:
        player_character.sprint()
    else:
        player_character.reload_stamina()
    player_character.attack()
    player_character.update_texture()

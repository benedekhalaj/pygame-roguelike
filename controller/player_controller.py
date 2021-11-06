from pygame import key
from pygame.constants import KEYDOWN
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
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        player_character.sprint()
    else:
        player_character.sprinting = False

    if keys[pygame.K_SPACE]:
        if player_character.sword.exist:
            if not player_character.attack_in_progress:
                player_character.attack_in_progress = True
                player_character.sword.texture_count = 0

def control_player(objects):
    player_character = objects['player'][0]

    change_player_on_input(player_character, objects)
    player_character.add_item_to_inventory(objects)
    player_character.take_damage(objects)
    if not player_character.sprinting:
        player_character.reload_stamina()
    player_character.set_sword_position()
    player_character.attack()
    player_character.update_texture()

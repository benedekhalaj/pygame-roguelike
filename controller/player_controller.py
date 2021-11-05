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
    if keys[pygame.K_SPACE]:
        if not player_character.attack_in_progress:
            player_character.attack_in_progress = True

def control_player(objects):
    player_character = objects['player'][0]

    change_player_on_input(player_character, objects)
    player_character.add_item_to_inventory(objects)
    player_character.take_damage(objects)
    player_character.set_sword_position()
    player_character.attack()

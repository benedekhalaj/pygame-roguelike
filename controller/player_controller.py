from model.player import player
from view import view
import pygame


def control_player(objects):
    for player_object in objects["player"]:
        player_character = player_object

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
        player_character.sword.visible = True
    else:
        player_character.sword.visible = False

    player_character.take_damage(objects)


def add_item_to_player_inventory(objects):
    for player_object in objects["player"]:
        player_character = player_object
    player_character.add_item_to_inventory(objects)


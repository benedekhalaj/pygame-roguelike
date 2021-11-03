from model.player import player
from view import view
import pygame


def control_player(objects):
    for object in objects:
        if object.type == 'player':
            player_character = object

    keys = view.get_input()

    if keys[pygame.K_LEFT]:
        player_character.move(objects, -player_character.velocity, 0)
    if keys[pygame.K_RIGHT]:
        player_character.move(objects, player_character.velocity, 0)
    if keys[pygame.K_UP]:
        player_character.move(objects, 0, -player_character.velocity)
    if keys[pygame.K_DOWN]:
        player_character.move(objects, 0, player_character.velocity)

from model.player import player
from view import terminal as view
import pygame


def get_player():
    return player.create_player()


def control_player(player):
    keys = view.get_input()

    if keys[pygame.K_LEFT]:
        player['x'] -= player['velocity']
    if keys[pygame.K_RIGHT]:
        player['x'] += player['velocity']
    if keys[pygame.K_UP]:
        player['y'] -= player['velocity']
    if keys[pygame.K_DOWN]:
        player['y'] += player['velocity']

    return player

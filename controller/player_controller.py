from model.player import player
from view import view
import pygame


def control_player(asterix):
    screen_size = (view.WINDOW_WIDTH, view.WINDOW_HEIGHT)
    for item in asterix:
        if item.type == 'player':
            player_character = item

    keys = view.get_input()

    if keys[pygame.K_LEFT]:
        player_character.move_left(asterix)
    if keys[pygame.K_RIGHT]:
        player_character.move_right(asterix)
    if keys[pygame.K_UP]:
        player_character.move_up(asterix)
    if keys[pygame.K_DOWN]:
        player_character.move_down(asterix)
    player_character.set_center(screen_size)

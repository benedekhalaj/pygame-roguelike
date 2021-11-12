import pygame
from model.map import map
from view import view
import pygame


def level_controller(objects, level, new_level, generate_player):
    keys = view.get_input()
    if keys[pygame.K_1]:
        save_map(objects, level)
        level = 1
        new_level = True
        generate_player = False
    elif keys[pygame.K_2]:
        save_map(objects, level)
        level = 2
        new_level = True
        generate_player = False
    elif keys[pygame.K_3]:
        save_map(objects, level)
        level = 3
        new_level = True
        generate_player = False
    return new_level, level, generate_player


def get_objects(level, unlocked_levels, objects, generate_player):
    game = map.Game(objects, (view.WINDOW_WIDTH, view.WINDOW_HEIGHT), view.COLORS, level, generate_player)
    if unlocked_levels < level:
        objects = game.create_map()
        unlocked_levels = level
    else:
        objects = game.load_map_file(level)
    return objects, unlocked_levels


def save_map(objects, level):
    map.Game.save_map_file(objects, level)

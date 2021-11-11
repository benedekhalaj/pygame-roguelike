import pygame
from model.map import map
from view import view
import pygame


def level_controller(objects, level, new_level):
    keys = view.get_input()
    if keys[pygame.K_1]:
        save_map(objects, level)
        level = 1
        new_level = True
    elif keys[pygame.K_2]:
        save_map(objects, level)
        level = 2
        new_level = True
    elif keys[pygame.K_3]:
        save_map(objects, level)
        level = 3
        new_level = True
    return new_level, level


def get_objects(level, unlocked_levels, objects):
    colors = view.COLORS
    screen_size = (view.WINDOW_WIDTH, view.WINDOW_HEIGHT)
    if unlocked_levels < level:
        map.Game(objects)
        objects = map.create_map(screen_size, colors, level)
        unlocked_levels = level
    else:
        objects = load_map(level, colors)
    return objects, unlocked_levels


def save_map(objects, level):
    map.save_map_file(objects, level)


def load_map(level, colors):
    return map.load_map_file(level, colors)

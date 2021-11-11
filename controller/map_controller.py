import pygame
from model.map import map
from view import view
import pygame


def level_controller(objects, level):
    keys = view.get_input()
    new_level = False
    if keys[pygame.K_1]:
        level = 2
        new_level = True
    elif keys[pygame.K_2]:
        level = 1
        new_level = True
    if new_level:
        save_map(objects, level)
    return new_level, level


def get_objects(level, objects, new_level):
    colors = view.COLORS
    screen_size = (view.WINDOW_WIDTH, view.WINDOW_HEIGHT)
    if new_level:
        map.Game(level, objects)
        objects = map.create_map(screen_size, colors, level)
    else:
        objects = load_map(level, colors)
    new_level = False
    return objects, new_level


def save_map(objects, level):
    map.save_map_file(objects, level)


def load_map(level, colors):
    return map.load_map_file(level, colors)

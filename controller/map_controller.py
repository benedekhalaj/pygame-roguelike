from model.map import map
from view import view


def get_objects():
    colors = view.COLORS
    screen_size = (view.WINDOW_WIDTH, view.WINDOW_HEIGHT)
    return map.create_map(screen_size, colors)


def save_map(objects):
    map.save_game(objects)
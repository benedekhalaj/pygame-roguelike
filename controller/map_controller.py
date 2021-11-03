from model.map import map
from view import view


def get_map():
    colors = view.COLORS
    screen_size = (view.WINDOW_WIDTH, view.WINDOW_HEIGHT)
    return map.create_map(screen_size, colors)

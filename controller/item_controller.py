from model.items import items
from view import terminal as view


def get_rectangles():
    return items.create_rectangles(view.WHITE, view.SCREEN_WIDTH)


def get_keys():
    return items.create_keys(view.YELLOW)

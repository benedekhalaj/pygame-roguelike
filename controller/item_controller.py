from model.items import items
from view import terminal as view


def get_white_rectangle():
    return items.Rectangle(view.WHITE, (100, 100, 64, 64))

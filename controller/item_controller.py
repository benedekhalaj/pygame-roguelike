from model.items import items
from view import terminal as view


def get_rectangles():
    return items.create_rectangles(view.WHITE, view.SCREEN_WIDTH)


def get_items():
    game_items = []
    game_items.extend(items.create_keys(view.YELLOW))
    game_items.extend(items.create_health_potions(view.RED))
    game_items.extend(items.create_chests(view.GREEN))
    return game_items

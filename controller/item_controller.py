from model.items import items
from view import terminal as view


def get_rectangles():
    obstacles = []
    obstacles.append(items.Rectangle(view.WHITE, (100, 100, 50, 50)))
    obstacles.append(items.Rectangle(view.WHITE, (150, 100, 50, 50)))
    obstacles.append(items.Rectangle(view.WHITE, (200, 100, 50, 50)))
    obstacles.append(items.Rectangle(view.WHITE, (200, 150, 50, 50)))
    obstacles.append(items.Rectangle(view.WHITE, (200, 200, 50, 50)))
    return obstacles

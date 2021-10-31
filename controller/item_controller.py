from model.items import items
from view import terminal as view


def get_rectangles():
    obstacles = []
    size = 25
    color = view.WHITE
    for index in range(0, view.SCREEN_WIDTH, size):
        obstacles.append(items.Rectangle(color, (index, 0, size, size)))
        obstacles.append(items.Rectangle(color, (0, index, size, size)))
        obstacles.append(items.Rectangle(color, (index, view.SCREEN_WIDTH - size, size, size)))

    return obstacles

from model.screen import screen
from view import terminal as view


def get_screen():
    return screen.Screen(view.BLACK, [0, 0, view.SCREEN_WIDTH, view.SCREEN_HEIGHT])

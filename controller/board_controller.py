from model.board import board
from view import view


def get_board():
    screen_size = (view.WINDOW_WIDTH, view.WINDOW_HEIGHT)
    return board.create_board(screen_size)
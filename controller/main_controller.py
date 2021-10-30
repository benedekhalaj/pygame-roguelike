from view import terminal as view
from controller import item_controller, npc_controller, player_controller
import pygame


def init_pygame():
    pygame.init()
    window = view.set_mode()
    view.set_caption('The Curse of Mighty Python')
    return window


def set_pygame_settings(run):
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    return run


def main():
    window = init_pygame()
    player = player_controller.get_player()
    white_rectangle = item_controller.get_white_rectangle()

    run = True
    while run:
        run = set_pygame_settings(run)
        player_controller.control_player(player)
        view.display_screen(window, player, white_rectangle)

    pygame.quit()

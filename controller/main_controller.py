from view import view
from controller import board_controller, npc_controller, player_controller, item_controller
import pygame



CLOCK = pygame.time.Clock()
FPS = 60


def init_pygame():
    pygame.init()
    window = view.set_display_mode()
    view.set_display_caption('The Curse of Mighty Python')
    return window


def set_fps():
    CLOCK.tick(FPS)


def quit_game(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                run = False

    return run


def main():
    window = init_pygame()
    asterix = board_controller.get_board()

    run = True
    while run:
        set_fps()
        run = quit_game(run)
        player_controller.control_player(asterix)
        view.display_background(window)
        view.display_asterix(window, asterix)
        view.refresh_display()
    pygame.quit()

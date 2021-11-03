from view import view
from controller import player_controller, map_controller, item_controller
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

    run = True
    while run:
        set_fps()
        run = quit_game(run)
    pygame.quit()

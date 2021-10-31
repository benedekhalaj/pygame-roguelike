from view import terminal as view
from controller import item_controller, npc_controller, player_controller, screen_controller
import pygame


CLOCK = pygame.time.Clock()


def init_pygame():
    pygame.init()
    window = view.set_mode()
    view.set_caption('The Curse of Mighty Python')
    return window


def set_pygame_settings(run):
    CLOCK.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = view.get_input()
    if keys[pygame.K_q]:
        run = False

    return run


def main():
    window = init_pygame()
    player = player_controller.get_player()
    screen = screen_controller.get_screen()
    obstacles = item_controller.get_rectangles()
    entities = [player] + obstacles

    run = True
    while run:
        run = set_pygame_settings(run)
        player_controller.control_player(player, screen, obstacles)
        view.display_screen(window, entities)

    pygame.quit()

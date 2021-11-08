from view import view
from controller import player_controller, map_controller, item_controller, enemy_controller, npc_controller
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


def quit_game(run, objects):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                run = False

    player_character = objects['player'][0]
    if player_character.health < 1:
        print('You are dead')
        run = False

    return run


def pause_game(pause, objects):
    pause = player_controller.control_inventory(objects, pause)
    return pause


def main():
    window = init_pygame()
    objects = map_controller.get_objects()

    run = True
    pause = False
    while run:
        set_fps()
        run = quit_game(run, objects)
        pause = pause_game(pause, objects)
        if not pause:
            player_controller.control_player(objects)
            enemy_controller.control_enemy(objects)
            item_controller.control_item(objects)
            npc_controller.control_npc(objects)
        view.display_everything(window, objects, pause)
    pygame.quit()

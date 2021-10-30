from model.player import player
from view import terminal as view
import pygame


def get_colors():
    return [view.RED, view.BLUE, view.GREEN, view.YELLOW]


def get_player():
    return player.Player(view.RED)


def check_screen_boundaries(player, screen, direction):
    if direction == "left":
        return player.x > screen.x
    elif direction == "right":
        return player.x + player.width < screen.x + screen.width
    elif direction == "up":
        return player.y > screen.y
    elif direction == "down":
        return player.y + player.height < screen.y + screen.height


def control_player(player, screen):
    keys = view.get_input()

    if keys[pygame.K_LEFT] and check_screen_boundaries(player, screen, "left"):
        player.move_left()
    if keys[pygame.K_RIGHT] and check_screen_boundaries(player, screen, "right"):
        player.move_right()
    if keys[pygame.K_UP] and check_screen_boundaries(player, screen, "up"):
        player.move_up()
    if keys[pygame.K_DOWN] and check_screen_boundaries(player, screen, "down"):
        player.move_down()
    if keys[pygame.K_LSHIFT]:
        player.sprint()
    else:
        player.walk()


def change_player_color(player, timer):
    keys = view.get_input()

    seconds = 0.2

    if timer > seconds * 60:
        timer = 0

    if timer == 0:
        if keys[pygame.K_SPACE]:
            player.change_color(get_colors())
            timer += 1
    else:
        timer += 1
    return timer

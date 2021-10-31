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


def control_player(player, screen, obstacles):
    keys = view.get_input()

    if keys[pygame.K_LEFT] and check_screen_boundaries(player, screen, "left"):
        player.move(obstacles, -2, 0)
    if keys[pygame.K_RIGHT] and check_screen_boundaries(player, screen, "right"):
        player.move(obstacles, 2, 0)
    if keys[pygame.K_UP] and check_screen_boundaries(player, screen, "up"):
        player.move(obstacles, 0, -2)
    if keys[pygame.K_DOWN] and check_screen_boundaries(player, screen, "down"):
        player.move(obstacles, 0, 2)

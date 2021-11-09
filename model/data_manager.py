import pygame


def open_file(filename: str):
    """opening a given file. reads it and give it back by splitlines.

    Returns: list of list
    """

    with open(filename, "r") as file:
        return file.read().splitlines()


def open_csv_file(filename: str):
    with open(filename, "r") as file:
        file = file.read().splitlines()
        return [char.split(',') for char in file]


def save_csv_file(filename: str, file: list):
    """creates a .csv file"""

    with open(filename, "w") as csv_file:
        for line in file:
            csv_file.write(",".join(line))
            csv_file.write("\n")


def save_game_to_csv_file(filename, game_file: dict):

    with open(f"{filename}_save.csv", "w") as file:
        for line in game_file:
            for object in line:
                file.write(f"{object}\n")

def open_image(path, filename=''):
    return pygame.image.load(f'{path}{filename}')


def open_sfx(path, filename=''):
    return pygame.mixer.Sound(f'{path}{filename}')

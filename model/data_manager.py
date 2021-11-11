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
        for object in game_file:
            texture_id = object[0]
            x = object[1]
            y = object[2]
            file.write(f"{texture_id}\t{x}\t{y}\n")


def load_game_from_csv_file(file_path):
    with open(f"{file_path}_save.csv", "r") as file:
        file = file.read().splitlines()
        return file


def open_image(path, filename=''):
    return pygame.image.load(f'{path}{filename}')


def open_sfx(path, filename=''):
    return pygame.mixer.Sound(f'{path}{filename}')

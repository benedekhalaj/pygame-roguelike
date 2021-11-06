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


def open_image(path, filename=''):
    return pygame.image.load(f'{path}{filename}')

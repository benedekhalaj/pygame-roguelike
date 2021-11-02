from types import coroutine
from model import data_manager, util
import pygame

from model.player.player import Player

def create_map():
    text_map = data_manager.file_opener("model/board/map_file/map.txt")
    map_sings = data_manager.file_opener("model/board/map_file/map_description.csv")
    map_sings_dict = {}
    for item in map_sings:
        item = item.split(":")
        map_sings_dict[item[0]] = item[1]
    return text_map, map_sings_dict


def create_board(screen_size):
    text_map, map_sign_dict = create_map()
    character_height = 32
    character_width = 32
    map_width = character_width * len(text_map)
    map_height = character_height * len(text_map[0])
    player_position = find_player_position(text_map)


    asterix = []

    for row_place, line in enumerate(text_map):
        for col_place, char in enumerate(line):
            y = ((row_place - player_position[1]) * character_height) + (screen_size[1] / 2 - character_height / 2)
            x = ((col_place - player_position[0]) * character_width) + (screen_size[0] / 2 - character_width / 2)
            position = (x, y, character_width, character_height)
            picture_name = map_sign_dict[char]
            if char == "x":
                asterix.append(util.Player(position, util.RED))
            elif char == "0":
                asterix.append(util.Wall(position, util.BLUE))
            elif char == "1":
                asterix.append(util.Wall(position, util.YELLOW))
            elif char == "2":
                asterix.append(util.Chest(position, util.GREEN))
            elif char == " ":
                asterix.append(util.Floor(position, util.WHITE))
    return asterix
                
# pygame.image.load(f"model/board/textures/{picture_name}.png")


def find_player_position(text_map: list):
    player_symbol = 'x'
    for line_index, line in enumerate(text_map):
        if player_symbol in line:
            x = line.index(player_symbol)
            y = line_index
            return (x, y)
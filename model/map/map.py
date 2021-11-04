import model.data_manager as data_manager
import model.enemy.enemy as enemy
import model.item.item as items
import model.player.player as player


def generate_map():
    text_map = data_manager.open_file("model/map/map_file/map.txt")
    map_sings = data_manager.open_file("model/map/map_file/map_description.csv")
    map_sings_dict = {}
    for item in map_sings:
        item = item.split(":")
        map_sings_dict[item[0]] = item[1]
    return text_map, map_sings_dict


def create_map(screen_size, colors):
    text_map, map_sign_dict = generate_map()
    character_height = 32
    character_width = 32
    player_position = find_player_position(text_map)
    objects = {}
    floor_list = []
    enemies_list = []
    player_list = []
    outer_walls_list = []
    inner_walls_list = []
    chests_list = []
    keys_list = []
    for row_place, line in enumerate(text_map):
        for col_place, char in enumerate(line):
            y = ((row_place - player_position[1]) * character_height) + (screen_size[1] / 2 - character_height / 2)
            x = ((col_place - player_position[0]) * character_width) + (screen_size[0] / 2 - character_width / 2)
            position = (x, y, character_width, character_height)
            character_name = map_sign_dict[char]
            floor_list.append(items.Floor(position, colors.WHITE))
            if character_name == "Player":
                player_list.append(player.Player(position, (colors.RED, colors.ORANGE, colors.PURPLE)))
            elif character_name == "Outer_Wall_1":
                outer_walls_list.append(items.Wall(position, colors.BLUE))
            elif character_name == "Inner_Wall_1":
                inner_walls_list.append(items.Wall(position, colors.YELLOW))
            elif character_name == "Chest":
                chests_list.append(items.Chest(position, colors.GREEN))
            elif character_name == "Key":
                keys_list.append(items.Key(position, colors.MAGENTA))
            elif character_name == "Enemy":
                enemies_list.append(enemy.Enemy(position, colors.BROWN))

    objects.update({"floor": floor_list,
                    "walls": outer_walls_list + inner_walls_list,
                    "items": chests_list + keys_list,
                    "enemies": enemies_list,
                    "player": player_list
                    })
    # objects = floor + outer_walls + inner_walls + chests + keys + enemies + player
    return objects


def find_player_position(text_map: list):
    player_symbol = 'x'
    for line_index, line in enumerate(text_map):
        if player_symbol in line:
            x = line.index(player_symbol)
            y = line_index
            return (x, y)












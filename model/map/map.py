from model import data_manager, blueprint


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
    floor = []
    enemies = []
    player = []
    outer_walls = []
    inner_walls = []
    chests = []
    keys = []
    for row_place, line in enumerate(text_map):
        for col_place, char in enumerate(line):
            y = ((row_place - player_position[1]) * character_height) + (screen_size[1] / 2 - character_height / 2)
            x = ((col_place - player_position[0]) * character_width) + (screen_size[0] / 2 - character_width / 2)
            position = (x, y, character_width, character_height)
            character_name = map_sign_dict[char]
            floor.append(blueprint.Floor(position, colors.WHITE))
            if character_name == "Player":
                player.append(blueprint.Player(position, (colors.RED, colors.ORANGE, colors.PURPLE)))
            elif character_name == "Outer_Wall_1":
                outer_walls.append(blueprint.Wall(position, colors.BLUE))
            elif character_name == "Inner_Wall_1":
                inner_walls.append(blueprint.Wall(position, colors.YELLOW))
            elif character_name == "Chest":
                chests.append(blueprint.Chest(position, colors.GREEN))
            elif character_name == "Key":
                keys.append(blueprint.Key(position, colors.MAGENTA))
            elif character_name == "Enemy":
                enemies.append(blueprint.Enemy(position, colors.BROWN))

    objects.update({"floor": floor,
                    "walls": outer_walls + inner_walls,
                    "items": chests + keys,
                    "enemies": enemies,
                    "player": player
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

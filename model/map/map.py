import model.data_manager as data_manager
import model.enemy.enemy as enemy
import model.item.item as items
import model.player.player as player


def generate_map():
    text_map = data_manager.open_file("model/map/map_file/base_level_0.txt")
    map_sings = data_manager.open_file("model/map/map_file/map_description.csv")
    map_sings_dict = {}
    for item in map_sings:
        if (":") not in item:
            continue
        item = item.split(":")
        map_sings_dict[item[0]] = item[1]
    return text_map, map_sings_dict


def create_map(screen_size, colors):
    text_map, map_sign_dict = generate_map()
    character_height = 64
    character_width = 64
    player_position = find_player_position(text_map)
    objects = {}
    floor_list = []
    enemies_list = []
    player_list = []
    walls_list = []
    chests_list = []
    potion_list = []
    keys_list = []
    door_list = []
    sword_list = []
    character_direction_name = [
                                map_sign_dict["L"],
                                map_sign_dict["R"],
                                map_sign_dict["U"],
                                map_sign_dict["D"]
                                ]
    for row_place, line in enumerate(text_map):
        for col_place, char in enumerate(line):
            y = ((row_place - player_position[1]) * character_height) + (screen_size[1] / 2 - character_height / 2)
            x = ((col_place - player_position[0]) * character_width) + (screen_size[0] / 2 - character_width / 2)
            position = (x, y, character_width, character_height)
            character_name = map_sign_dict[char]
            if character_name != 'Void':
                floor_list.append(items.Floor(position, colors))
            if character_name in character_direction_name:
                floor_list.append(items.Floor(position, colors))
                continue
            if character_name == "Player":
                player_list.append(player.Player(position, colors, screen_size))
            elif "wall" in character_name:
                walls_list.append(items.Wall(position, character_name, colors))
            elif character_name == "Chest":
                chests_list.append(items.Chest(position, colors))
            elif character_name == "Key":
                keys_list.append(items.Key(position, character_name, colors))
            elif character_name == "health_potion":
                potion_list.append(items.Health_Potion(position, character_name, colors))
            elif character_name == "Door":
                door_list.append(items.Door(position, character_name, colors))
            elif character_name == "Zombie_Enemy":
                char = text_map[row_place][col_place + 1]
                character_name = map_sign_dict[char]
                if character_name == "Right":
                    enemies_list.append(enemy.Standard_Enemy(position, colors, ("right", 60)))
                elif character_name == "Left":
                    enemies_list.append(enemy.Standard_Enemy(position, colors, ("left", 60)))
                elif character_name == "Down":
                    enemies_list.append(enemy.Standard_Enemy(position, colors, ("down", 30)))
                elif character_name == "Up":
                    enemies_list.append(enemy.Standard_Enemy(position, colors, ("up", 30)))
            elif character_name == "Eye_Enemy":
                enemies_list.append(enemy.Eye_Enemy(position, colors))
            elif character_name == "Sword":
                sword_list.append(items.Sword(position,character_name, colors))



    objects.update({"floor": floor_list,
                    "walls": walls_list,
                    "doors": door_list,
                    "items": chests_list + keys_list + sword_list + potion_list,
                    "enemies": enemies_list,
                    "player": player_list
                    })
    return objects


def find_player_position(text_map: list):
    player_symbol = 'x'
    for line_index, line in enumerate(text_map):
        if player_symbol in line:
            x = line.index(player_symbol)
            y = line_index
            return (x, y)

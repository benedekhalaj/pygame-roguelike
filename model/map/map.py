import model.data_manager as data_manager
import model.enemy.enemy as enemy
import model.item.item as items
import model.player.player as player
import model.npc.npc as npc


LEVEL_1 = 'map'
LEVEL_2 = 'level_2'


def generate_map():
    file_path = f"model/map/map_file/{LEVEL_1}"
    text_map = data_manager.open_csv_file(f"{file_path}.csv")
    map_sings = data_manager.open_file("model/map/map_file/map_description.csv")
    map_sings_dict = create_map_sign_dict(map_sings)
    return text_map, map_sings_dict, file_path


def create_map(screen_size, colors):
    text_map, map_sign_dict, file_name = generate_map()
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
    npc_list = []
    for row_place, line in enumerate(text_map):
        for col_place, char in enumerate(line):
            y = ((row_place - player_position[1]) * character_height) + (screen_size[1] / 2 - character_height / 2)
            x = ((col_place - player_position[0]) * character_width) + (screen_size[0] / 2 - character_width / 2)
            position = (x, y, character_width, character_height)
            character_name = map_sign_dict[char][0]
            file_path = map_sign_dict[char][1]

            if character_name != 'Void':
                floor_list.append(items.Floor(position, map_sign_dict["1"][1], colors))

            if character_name == "Player":
                player_list.append(player.Player(position, file_path, colors, screen_size, file_name))

            elif "Wall" in character_name:
                walls_list.append(items.Wall(position, file_path, colors))

            elif character_name == "Chest":
                chests_list.append(items.Chest(position, file_path, colors))
            elif character_name == "Key":
                keys_list.append(items.Key(position, file_path, colors))
            elif character_name == "Health_Potion":
                potion_list.append(items.Health_Potion(position, file_path, colors))
            elif character_name == "Door":
                door_list.append(items.Door(position, file_path, character_name, colors))
            elif character_name == "Sword":
                sword_list.append(items.Sword(position, file_path, character_name, colors))

            elif character_name == "Zombie_Right":
                enemies_list.append(enemy.Zombie_Enemy(position, file_path, colors, ("right", 60)))
            elif character_name == "Zombie_Left":
                enemies_list.append(enemy.Zombie_Enemy(position, file_path, colors, ("left", 60)))
            elif character_name == "Zombie_Down":
                enemies_list.append(enemy.Zombie_Enemy(position, file_path, colors, ("down", 30)))
            elif character_name == "Zombie_Up":
                enemies_list.append(enemy.Zombie_Enemy(position, file_path, colors, ("up", 30)))
            # elif character_name == "Eye_Enemy":
            #     enemies_list.append(enemy.Eye_Enemy(position, file_path, colors))
            # elif character_name == 'Shooter_Enemy':
            #     enemies_list.append(enemy.Shooter_Enemy(position, file_path, colors, ("right", "down")))
            elif character_name == 'Shooter_Vertical_Right':
                enemies_list.append(enemy.Shooter_Enemy(position, file_path, colors, ("down", "right")))
            elif character_name == 'Shooter_Vertical_Left':
                enemies_list.append(enemy.Shooter_Enemy(position, file_path, colors, ("down", "left")))
            elif character_name == 'Shooter_Horizontal_Up':
                enemies_list.append(enemy.Shooter_Enemy(position, file_path, colors, ("right", "up")))
            elif character_name == 'Shooter_Horizontal_Down':
                enemies_list.append(enemy.Shooter_Enemy(position, file_path, colors, ("right", "down")))

            elif character_name == 'Brain_Collector_NPC':
                npc_list.append(npc.Brain_Collector_NPC(position, colors))

    objects.update({"floor": floor_list,
                    "walls": walls_list,
                    "doors": door_list,
                    "items": chests_list + keys_list + sword_list + potion_list,
                    "enemies": enemies_list,
                    "player": player_list,
                    "npc": npc_list
                    })
    return objects


def create_map_sign_dict(map_signs):
    map_sings_dict = {}
    for item in map_signs:
        if (":") not in item:
            continue
        item = item.split(":	")
        map_sings_dict[item[0]] = [item[1], item[2]]
    return map_sings_dict


def find_player_position(text_map: list):
    player_symbol = '0'
    for line_index, line in enumerate(text_map):
        if player_symbol in line:
            x = line.index(player_symbol)
            y = line_index
            return (x, y)


def save_game(object_types: dict):
    file_path = object_types["player"][0].file_path
    object_list = []
    for objects in object_types.values():
        objects_row_list = []
        for object in objects:
            if objects == file_path:
                continue
            if object.visible is False:
                continue
            if object.type == "brain_collector":
                continue
            type = object.type
            visible = str(object.visible)
            x = str(object.rect.x)
            y = str(object.rect.y)
            item = (type, visible, x, y)
            objects_row_list.append(item)
        object_list.append(objects_row_list)
    data_manager.save_game_to_csv_file(file_path, object_list)

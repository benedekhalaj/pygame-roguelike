from pygame import Color
import model.data_manager as data_manager
import model.enemy.enemy as enemy
import model.item.item as items
import model.player.player as player
import model.npc.npc as npc


CHARACTER_WIDTH = 64
CHARACTER_HEIGHT = 64


class Game():
    def __init__(self, objects, screen_size, colors, level, generate_player):
        self.player = objects["player"]
        self.generate_player = generate_player
        self.actual_level = level
        self.objects = objects
        self.screen_size = screen_size
        self.colors = colors
        self.map_signs = data_manager.open_file("model/map/map_file/map_description.csv")
        self.map_sings_dict = self.create_map_sign_dict()

    def generate_map(self, level):
        file_path = f"model/map/map_file/level_{level}/level_{level}"
        text_map = data_manager.open_csv_file(f"{file_path}.csv")
        return text_map, file_path

    def create_map(self):
        text_map, map_file_path = self.generate_map(self.actual_level)
        player_position = self.find_player_position(text_map)

        reload_map_datas = [[map_file_path]]
        for row_place, line in enumerate(text_map):
            for col_place, texture_id in enumerate(line):
                y = ((row_place - player_position[1]) * CHARACTER_HEIGHT) + (self.screen_size[1] / 2 - CHARACTER_HEIGHT / 2)
                x = ((col_place - player_position[0]) * CHARACTER_WIDTH) + (self.screen_size[0] / 2 - CHARACTER_WIDTH / 2)
                position = (x, y, CHARACTER_WIDTH, CHARACTER_HEIGHT)
                character_name = self.map_sings_dict[texture_id][0]
                if character_name == "Void":
                    continue
                texture_file_path = self.map_sings_dict[texture_id][1]
                needs_floor = True
                object_datas = [position, texture_file_path, character_name, texture_id, needs_floor]
                reload_map_datas.append(object_datas)
        return self.create_objects(reload_map_datas)

    def create_map_sign_dict(self):
        map_sings_dict = {}
        for item in self.map_signs:
            if (":") not in item:
                continue
            item = item.split(":	")
            map_sings_dict[item[0]] = [item[1], item[2]]
        return map_sings_dict

    def find_player_position(self, text_map: list):
        player_symbol = '0'
        for line_index, line in enumerate(text_map):
            if player_symbol in line:
                x = line.index(player_symbol)
                y = line_index
                return (x, y)

    def save_map_file(object_types: dict, level):
        map_file_path = f"model/map/map_file/level_{level}/level_{level}"
        object_list = []
        for objects in object_types.values():
            for object in objects:
                if objects == map_file_path:
                    continue
                if object.type == "player":
                    Game.objects_player = object
                    continue
                if object.visible is False:
                    continue
                if object.type == "brain":
                    continue
                x = str(object.rect.x)
                y = str(object.rect.y)
                id = str(object.texture_id)
                item = (id, x, y)
                object_list.append(item)
        data_manager.save_game_to_csv_file(map_file_path, object_list)

    def load_map_file(self, level):
        map_file_path = f"model/map/map_file/level_{level}/level_{level}"
        file = data_manager.load_game_from_csv_file(map_file_path)

        reload_map_datas = [map_file_path]
        for line in file:
            object = line.split("\t")
            texture_id = object[0]
            x = int(object[1])
            y = int(object[2])
            texture_file_path = self.map_sings_dict[texture_id][1]
            character_name = self.map_sings_dict[texture_id][0]
            position = (x, y, CHARACTER_WIDTH, CHARACTER_HEIGHT)
            if texture_id == "1":
                needs_floor = True
            else:
                needs_floor = False
            object_datas = [position, texture_file_path, character_name, texture_id, needs_floor]
            reload_map_datas.append(object_datas)
        return self.create_objects(reload_map_datas)

    def create_objects(self, map_datas: list):
        map_file_path = map_datas[0]

        objects = {}
        floor_list = []
        enemies_list = []
        player_list = []
        walls_list = []
        chests_list = []
        potion_list = []
        keys_list = []
        door_list = []
        gate_list = []
        sword_list = []
        npc_list = []
        for data_list in map_datas[1::]:
            position = data_list[0]
            texture_file_path = data_list[1]
            character_name = data_list[2]
            texture_id = data_list[3]
            needs_Floor = data_list[4]
            if needs_Floor:
                floor_list.append(items.Floor("1", position, self.map_sings_dict["1"][1], self.colors))

            if character_name == "Player":
                player_list.append(player.Player(texture_id, position, texture_file_path, self.colors, self.screen_size, map_file_path))

            elif "Wall" in character_name:
                walls_list.append(items.Wall(texture_id, position, texture_file_path, self.colors))

            elif character_name == "Chest":
                chests_list.append(items.Chest(texture_id, position, texture_file_path, self.colors))
            elif character_name == "Key" or character_name == "Rare_Key":
                keys_list.append(items.Key(texture_id, position, texture_file_path, self.colors))
            elif character_name == "Health_Potion":
                potion_list.append(items.Health_Potion(texture_id, position, texture_file_path, self.colors))
            elif character_name == "Door":
                door_list.append(items.Door(texture_id, position, texture_file_path, self.colors))
            elif character_name == "Gate":
                gate_list.append(items.Gate(texture_id, position, texture_file_path, self.colors))
            elif character_name == "Sword":
                sword_list.append(items.Sword(texture_id, position, texture_file_path, character_name, self.colors))

            elif character_name == "Zombie_Right":
                enemies_list.append(enemy.Zombie_Enemy(texture_id, position, texture_file_path, self.colors, ("right", 60)))
            elif character_name == "Zombie_Left":
                enemies_list.append(enemy.Zombie_Enemy(texture_id, position, texture_file_path, self.colors, ("left", 60)))
            elif character_name == "Zombie_Down":
                enemies_list.append(enemy.Zombie_Enemy(texture_id, position, texture_file_path, self.colors, ("down", 30)))
            elif character_name == "Zombie_Up":
                enemies_list.append(enemy.Zombie_Enemy(texture_id, position, texture_file_path, self.colors, ("up", 30)))

            elif character_name == "Eyeball_Up":
                enemies_list.append(enemy.Eye_Enemy(texture_id, position, texture_file_path, self.colors))
            elif character_name == "Eyeball_Down":
                enemies_list.append(enemy.Eye_Enemy(texture_id, position, texture_file_path, self.colors))
            elif character_name == "Eyeball_Left":
                enemies_list.append(enemy.Eye_Enemy(texture_id, position, texture_file_path, self.colors))
            elif character_name == "Eyeball_Right":
                enemies_list.append(enemy.Eye_Enemy(texture_id, position, texture_file_path, self.colors,))
            # elif character_name == 'Shooter_Enemy':
            #     enemies_list.append(enemy.Shooter_Enemy(position, file_path, colors, ("right", "down")))
            elif character_name == 'Shooter_Vertical_Right':
                enemies_list.append(enemy.Shooter_Enemy(texture_id, position, texture_file_path, self.colors, ("down", "right")))
            elif character_name == 'Shooter_Vertical_Left':
                enemies_list.append(enemy.Shooter_Enemy(texture_id, position, texture_file_path, self.colors, ("down", "left")))
            elif character_name == 'Shooter_Horizontal_Up':
                enemies_list.append(enemy.Shooter_Enemy(texture_id, position, texture_file_path, self.colors, ("right", "up")))
            elif character_name == 'Shooter_Horizontal_Down':
                enemies_list.append(enemy.Shooter_Enemy(texture_id, position, texture_file_path, self.colors, ("right", "down")))

            elif character_name == 'Brain_Collector_NPC':
                npc_list.append(npc.Brain_Collector_NPC(texture_id, position, self.colors))

        objects.update({"floor": floor_list,
                        "walls": walls_list,
                        "doors": door_list + gate_list,
                        "items": chests_list + keys_list + sword_list + potion_list,
                        "enemies": enemies_list,
                        "player": player_list,
                        "npc": npc_list
                        })
        if self.generate_player:
            self.player = objects["player"]
        else:
            objects["player"] = self.player
        return objects

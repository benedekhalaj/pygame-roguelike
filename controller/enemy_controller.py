from view import view
from model.enemy import enemy


def control_enemy(objects):
    for object in objects["enemies"]:
        enemy_character = object
    enemy_character.move()
    enemy_character.take_damage(objects)

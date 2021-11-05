from view import view
from model.enemy import enemy


def control_enemy(objects):
    for enemy_character in objects["enemies"]:
        enemy_character.move()
        enemy_character.take_damage(objects)

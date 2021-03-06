from view import view
from model.enemy import enemy


def control_enemy(objects):
    for enemy_character in objects["enemies"]:

        if enemy_character.type == 'standard':
            enemy_character.move(objects)
            enemy_character.take_damage(objects)
            enemy_character.update_hitbox()
            enemy_character.update_health_bar()
            enemy_character.update_texture()

        elif enemy_character.type == 'eye':
            enemy_character.set_facing(objects)
            enemy_character.take_damage(objects)

        elif enemy_character.type == 'shooter':
            enemy_character.move(objects)
            enemy_character.shoot(objects)
            enemy_character.take_damage(objects)
            enemy_character.delete_projectile()

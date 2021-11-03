from view import view
from model.enemy import enemy

def control_enemy(objects):
    for object in objects:
        if object.type == "enemy":
            enemy = object
    enemy.move()

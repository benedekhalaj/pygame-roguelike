from model.item import item
from view import view


def control_item(objects):
    for item in objects['items']:
        if item.type == 'brain':
            item.update_texture_count()

    for door in objects['doors']:
        if door.type == "gate" or door.type == "rare_gate":
            door.set_facing(objects)
        else:
            door.update_texture()

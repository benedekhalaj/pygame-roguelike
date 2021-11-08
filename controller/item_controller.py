from model.item import item
from view import view


def control_item(objects):
    for item in objects['items']:
        if item.type == 'brain':
            item.update_texture_count()

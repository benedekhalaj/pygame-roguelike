from view import view
from model.npc import npc


def control_npc(objects):
    for npc in objects['npc']:
        npc.talk_with_player(objects)
        npc.update_texture_count()

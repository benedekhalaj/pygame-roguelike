from model import data_manager, util


def create_rectangle(color, position):
    return {
        "color": color,
        "x": position[0],
        "y": position[1],
        "width": position[2],
        "height": position[3]
    }
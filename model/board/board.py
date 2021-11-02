from model import data_manager, util


def conver_map():
    """Rewrite the given map by the given strings.

    Returns: list of list
    """

    text_map = data_manager.file_opener("model/board/map_file/map.txt")
    csv_map_list = []
    for line in text_map:
        inner_list = []
        for coordinate in line:
            if coordinate == " ":
                inner_list.append("0")
            elif coordinate == "w":
                inner_list.append("1")
            elif coordinate == "i":
                inner_list.append("2")
            else:
                inner_list.append(str(int(coordinate) + 10))
        csv_map_list.append(inner_list)
    return csv_map_list


def save_csv_map():
    """Saves the given file into a .csv file

    Returns: nothing
    """

    data_manager.save_csv_file('model/board/map_file/map.csv', conver_map())

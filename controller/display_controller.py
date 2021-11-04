import view.view as view
import model.display.display as display


def display_stat(window, objects):
    colors = view.COLORS
    stat_background_rect = (view.STAT_WIDTH, view.STAT_HEIGHT)
    stat = {"stat": [display.Stat(stat_background_rect, window, colors)]}
    return stat


def stats(window, objects):
    colors = view.COLORS
    stat = display_stat(window, objects)
    x = stat["stat"][0].x
    y = stat["stat"][0].y
    return display.Stat.diplay_player_stat(colors, objects), x, y

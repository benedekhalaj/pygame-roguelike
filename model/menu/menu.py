from model import data_manager
import pygame


class Main_Menu():
    def __init__(self):
        pygame.font.init()
        self.type = 'menu'
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.x = 120
        self.y = screen / 1



# ________---------_________-----------_________-----------_________----------

def print_menu(screen, menu, current_line):
    coordinates = screen.getmaxyx()
    h = coordinates[0]
    w = coordinates[1]
    for index in range(len(menu)):
        y = h // 2 - len(menu) // 2
        x = w // 2 - len(menu[index]) // 2
        if index == current_line:
            screen.addstr(y + index, x, menu[index], curses.color_pair(1))
        else:
            screen.addstr(y + index, x, menu[index])


def main_menu(screen):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_line = 0
    menu = ['Play', 'Exit']
    while True:
        print_menu(screen, menu, current_line)
        screen.refresh()
        key = screen.getch()
        screen.clear()
        if key == curses.KEY_UP and current_line > 0:
            current_line -= 1
        elif key == curses.KEY_DOWN and current_line < len(menu) - 1:
            current_line += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_line == 0:
                pass
            elif current_line == 1:
                quit()


def main():
    curses.wrapper(main_menu)

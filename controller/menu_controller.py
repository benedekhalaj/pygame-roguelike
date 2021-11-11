import pygame
from model.menu import menu
from view import view


CLOCK = pygame.time.Clock()
FPS = 30

FONT_SIZE = 60


def play_background_music():
    pygame.mixer.init()
    pygame.mixer.music.load('sound/music/main_theme.WAV')
    pygame.mixer.music.play(loops=-1)


def stop_background_music():
    pygame.mixer.music.stop()


def create_textsurfaces(window, menu_items, current_line):
    textsurfaces = []
    for index, text in enumerate(menu_items):
        pygame.font.init()
        myfont = pygame.font.SysFont('ubuntumono', FONT_SIZE, True)
        if index == current_line:
            textsurfaces.append(myfont.render(text, False, view.COLORS.YELLOW))
        else:
            textsurfaces.append(myfont.render(text, False, view.COLORS.WHITE))
    return textsurfaces


def set_fps():
    CLOCK.tick(FPS)


def quit_menu(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                run = False

    return run


def control_menu(menu_items, current_line):
    keys = view.get_input()

    if keys[pygame.K_UP] and current_line > 0:
        current_line -= 1
    elif keys[pygame.K_DOWN] and current_line < len(menu_items) - 1:
        current_line += 1

    return current_line


def interact_in_menu(current_line, run):
    keys = view.get_input()

    if keys[pygame.K_RETURN]:
        if current_line == 0:
            run = False
        elif current_line == 1:
            quit()

    return run


def main_menu(window):
    play_background_music()
    menu_items = ['Play', 'Quit']
    current_line = 0
    window_width = view.WINDOW_WIDTH
    window_height = view.WINDOW_HEIGHT


    run = True
    while run:
        set_fps()
        run = quit_menu(run)

        current_line = control_menu(menu_items, current_line)

        run = interact_in_menu(current_line, run)

        view.display_background(window)

        textsurfaces = create_textsurfaces(window, menu_items, current_line)
        for index, surface in enumerate(textsurfaces):
            x_position = window_width // 2 - (len(menu_items[index]) * FONT_SIZE // 2) // 2
            y_position = window_height // 2 - (len(menu_items) * FONT_SIZE // 2) + (60 * index)
            window.blit(surface, (x_position, y_position))
        view.refresh_display()

    stop_background_music()

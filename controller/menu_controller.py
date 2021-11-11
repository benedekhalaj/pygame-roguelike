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


def create_textsurfaces(menu_items, current_line=''):
    textsurfaces = []
    for index, text in enumerate(menu_items):
        pygame.font.init()
        myfont = pygame.font.SysFont('ubuntumono', FONT_SIZE, True)
        if index == current_line:
            textsurfaces.append(myfont.render(text, False, view.COLORS.YELLOW))
        else:
            textsurfaces.append(myfont.render(text, False, view.COLORS.WHITE))
    return textsurfaces


def create_textsurface(text):
    pygame.font.init()
    myfont = pygame.font.SysFont('ubuntumono', FONT_SIZE, True)
    textsurface = myfont.render(text, False, view.COLORS.WHITE)
    return textsurface


def set_fps():
    CLOCK.tick(FPS)


def quit_menu(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                run = False

    return run


def control_menu(menu_items, current_line, can_press_button):
    keys = view.get_input()

    if can_press_button:
        if keys[pygame.K_UP] and current_line > 0:
            current_line -= 1
            can_press_button = False
        elif keys[pygame.K_DOWN] and current_line < len(menu_items) - 1:
            current_line += 1
            can_press_button = False

    return current_line, can_press_button


def interact_with_main_menu(window, current_line, run):
    keys = view.get_input()

    if keys[pygame.K_RETURN]:
        if current_line == 0:
            run = False
        elif current_line == 1:
            controls_menu(window)
        elif current_line == 2:
            quit()

    return run


def interact_with_controls_menu(controls_run):
    keys = view.get_input()

    if keys[pygame.K_BACKSPACE]:
        controls_run = False

    return controls_run


def update_menu_count(count, count_limit, can_press_button):
    if can_press_button == False:
        count += 1

    if count > count_limit:
        count = 0
        can_press_button = True

    return count, can_press_button


def controls_menu(window):
    window_width = view.WINDOW_WIDTH
    window_height = view.WINDOW_HEIGHT
    headline = 'CONTROLS'
    controls = ['Move up - UP ARROW',
                'Move down - DOWN ARROW',
                'Move right - RIGHT ARROW',
                'Move left - LEFT ARROW',
                '',
                'Attack - SPACE',
                'Sprint - LSHIFT, RSHIFT',
                'Inventory - I',
                'Drink Health Potion - H',
                '',
                '',
                'Press BACKSPACE to go back to Main Menu']

    headline_textsurface = create_textsurface(headline)
    textsurfaces = create_textsurfaces(controls)
    controls_run = True
    while controls_run:
        controls_run = quit_menu(controls_run)
        controls_run = interact_with_controls_menu(controls_run)

        view.display_background(window)
        window.blit(headline_textsurface, (window_width // 2 - (len(headline) * (FONT_SIZE // 2)) // 2, 20))
        for index, surface in enumerate(textsurfaces):
            x_position = window_width // 2 - (len(controls[index]) * FONT_SIZE // 2) // 2
            y_position = window_height // 2 - (len(controls) * FONT_SIZE // 2) + (FONT_SIZE * index)
            window.blit(surface, (x_position, y_position))
        view.refresh_display()


def main_menu(window):
    play_background_music()
    menu_items = ['Play', 'Controls', 'Quit']
    current_line = 0
    window_width = view.WINDOW_WIDTH
    window_height = view.WINDOW_HEIGHT
    headline = 'THE CURSE OF MIGHTY PYTHON'
    headline_textsurface = create_textsurface(headline)

    can_press_button = True
    control_count = 0
    control_count_limit = 3


    run = True
    while run:
        set_fps()
        run = quit_menu(run)

        current_line, can_press_button = control_menu(menu_items, current_line, can_press_button)

        control_count, can_press_button = update_menu_count(control_count, control_count_limit, can_press_button)
        if can_press_button:
            run = interact_with_main_menu(window, current_line, run)

        view.display_background(window)

        window.blit(headline_textsurface, (window_width // 2 - (len(headline) * (FONT_SIZE // 2)) // 2, 20))

        textsurfaces = create_textsurfaces(menu_items, current_line)
        for index, surface in enumerate(textsurfaces):
            x_position = window_width // 2 - (len(menu_items[index]) * FONT_SIZE // 2) // 2
            y_position = window_height // 2 - (len(menu_items) * FONT_SIZE // 2) + (FONT_SIZE * index)
            window.blit(surface, (x_position, y_position))
        view.refresh_display()

    stop_background_music()

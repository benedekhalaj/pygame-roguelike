import pygame
from model.menu import menu
from view import view


CLOCK = pygame.time.Clock()
FPS = 30


def play_background_music():
    pygame.mixer.init()
    pygame.mixer.music.load('sound/music/main_theme.WAV')
    pygame.mixer.music.play(loops=-1)


def stop_background_music():
    pygame.mixer.music.stop()


def create_font(window):
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Main Menu', False, view.COLORS.WHITE)
    return textsurface


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


def main_menu(window):
    # play_background_music()
    menu_text = create_font(window)

    run = True
    while run:
        set_fps()
        run = quit_menu(run)
        
        view.display_background(window)
        view.display_text(window, menu_text)
        view.refresh_display()

    stop_background_music()

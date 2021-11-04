import pygame
import pygame.freetype


class Stat():
    def __init__(self, stat_background_rect, window, colors):
        self.type = "stat"
        self.widht = stat_background_rect[0]
        self.height = stat_background_rect[1]
        self.size_widht, self.size_height = window.get_size()
        self.x = 0
        self.y = 0
        self.position = (self.x, self.y, self.widht, self.height)
        self.rect = pygame.Rect(self.x, self.y, self.widht, self.height)
        self.color = colors.BROWN
        self.visible = True

    def diplay_player_stat(colors, objects):
        font_type = 'couriernew'
        player_health = objects["player"][0].health
        font = pygame.font.SysFont(font_type, 30, True)
        # pygame.font.get_fonts()
        textsurface = font.render(f"{player_health} hp", False, (0, 0, 0))
        return textsurface

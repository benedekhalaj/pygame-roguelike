from model import data_manager
import pygame


class Brain_Collector_NPC():
    def __init__(self, position, colors):
        self.type = 'brain_collector'
        self.rect = pygame.Rect(position[0] - 64, position[1] - 64, 128, 128)
        self.color = colors.GREY
        self.texture = None
        self.brain_expectation = 42

        self.talking_in_progress = False
        self.has_mission = True

        self.visible = True

    def talk_with_player(self, objects):
        player = objects['player'][0]
        if self.has_mission:
            if self.rect.colliderect(player.rect):
                if not self.talking_in_progress:
                    if player.inventory.brains < self.brain_expectation:
                        print('Hello Dear! It seems like you haven\'t yet gathered all of the brains.')
                        print(f'{self.brain_expectation - player.inventory.brains} more to go!')
                        self.talking_in_progress = True
                    else:
                        self.has_mission = False
                        player.inventory.brains = 0
                        player.max_health += 1
                        player.health = player.max_health
                        print(f'Brains: {player.inventory.brains}')
                        print('Wow! You gathered all the brains I need!')
                        print('As a reward, I increase your maximum health by 1')

            else:
                self.talking_in_progress = False

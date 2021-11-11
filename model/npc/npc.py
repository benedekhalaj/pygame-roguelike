from model import data_manager
import pygame
import random


pygame.mixer.init()

SFX_NPC_2 = data_manager.open_sfx('sound/sfx/npc/npc2.ogg')
SFX_NPC_3 = data_manager.open_sfx('sound/sfx/npc/npc3.ogg')
SFX_NPC_4 = data_manager.open_sfx('sound/sfx/npc/npc4.ogg')
SFX_NPC_5 = data_manager.open_sfx('sound/sfx/npc/npc5.ogg')
SFX_NPC_6 = data_manager.open_sfx('sound/sfx/npc/npc6.ogg')
SFX_NPC_7 = data_manager.open_sfx('sound/sfx/npc/npc7.ogg')



class Brain_Collector_NPC():
    def __init__(self, texture_id, position, colors):
        self.type = 'brain_collector'
        self.x = position[0]
        self.y = position[1]
        self.width = position[2]
        self.height = position[3]
        self.rect = pygame.Rect(position[0], position[1], 128, 128)
        self.color = colors.GREY

        self.conversation = Conversation((self.rect.x, self.rect.y, self.rect.width, self.rect.height), colors.WHITE)

        self.texture_id = texture_id
        self.texture = [data_manager.open_image('model/map/textures/npcs/oldman_idle1.png'),
                        data_manager.open_image('model/map/textures/npcs/oldman_idle2.png')]
        self.texture_count = 0
        self.texture_count_limit = 60

        self.brain_expectation = 2

        self.has_met_player = False
        self.talking_in_progress = False
        self.has_mission = True

        self.visible = True

    def talk_with_player(self, objects):
        sounds = [SFX_NPC_2, SFX_NPC_3, SFX_NPC_4, SFX_NPC_5, SFX_NPC_6, SFX_NPC_7]
        player = objects['player'][0]
        if self.rect.colliderect(player.rect):
            if self.has_mission:
                if not self.talking_in_progress:
                    if not self.has_met_player:
                        self.has_met_player = True
                        self.talking_in_progress = True
                        self.conversation.text = ['Hello poor thing!',
                                                  'It seems like you would',
                                                  'use a little boost...',
                                                  'I can give you something',
                                                  'for giving me 42 brains!'
                                                  ]
                        random.choice(sounds).play()

                    elif player.inventory.brains < self.brain_expectation:
                        self.talking_in_progress = True
                        self.conversation.text = ['It seems like you haven\'t',
                                                  'yet gathered all of the',
                                                  'brains yet...',
                                                  f'{self.brain_expectation - player.inventory.brains} more to go!'
                                                  ]
                        random.choice(sounds).play()

                    else:
                        self.talking_in_progress = True
                        self.has_mission = False
                        player.inventory.brains = 0
                        player.max_health += 1
                        player.health = player.max_health
                        self.conversation.text = ['Wow, that is something!',
                                                  'As a reward, I increase',
                                                  'your maximum health by 1!'
                                                  ]
                        random.choice(sounds).play()

        else:
            self.talking_in_progress = False

    def update_texture_count(self):
        if self.texture_count + 1 >= self.texture_count_limit:
            self.texture_count = 0

        self.texture_count += 1

    def update_conversation(self):
        if self.talking_in_progress:
            self.conversation.visible = True
        else:
            self.conversation.visible = False


class Conversation():
    def __init__(self, position, color):
        self.type = 'conversation'

        self.width = 256
        self.height = 128
        self.x = position[0] - self.width / 1.4
        self.y = position[1] - self.height + 10

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = color
        self.texture = data_manager.open_image('model/map/textures/npcs/conversation.png')

        self.text = []
        self.visible = False

# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.display
from xml.dom.minidom import Entity
from typing import List

from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_HEIGHT
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: List[Entity] = []  # Inicializa uma lista vazia de entidades
        self.entity_list.extend(EntityFactory.get_entity('level1Bg'))
        self.timeout = 2000  # 20 segundos

    def run(self, clock):  # Agora aceita o argumento clock
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # printed text
            text_size = 14  # Define text_size aqui
            self.level_text(text_size, f'{self.name} - Timeout: {self.timeout / 100 :.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(text_size, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(text_size, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        # Corrigindo a chamada para incluir o argumento antialias
        text_surf: Surface = text_font.render(text, True, text_color)  # O True ativa o antialiasing
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

# Level.py

#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.display
from xml.dom.minidom import Entity
from typing import List
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: List[Entity] = []  # Inicializa uma lista vazia de entidades
        self.entity_list.extend(EntityFactory.get_entity('level1Bg'))

    def run(self, clock):
        while True:
            # Verifica se a lista de entidades foi carregada corretamente
            if not self.entity_list:
                print("Nenhuma entidade foi carregada.")  # Debug para verificar a lista
                return  # Encerra o loop caso não haja entidades

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            pygame.display.flip()
            clock.tick(60)  # Controle de FPS

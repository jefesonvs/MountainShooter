# EntityFactory.py

#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Backgound import Background
from code.Const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):  # Corrigir o nome para 'level1Bg'
        if entity_name == 'level1Bg':  # Verifique o nome da entidade
            list_bg = []
            for i in range(7):
                list_bg.append(Background(f'level1Bg{i}', (0, 0)))
                list_bg.append(Background(f'level1Bg{i}', (WIN_WIDTH, 0)))
            return list_bg
        else:
            return []  # Retorna uma lista vazia se o nome da entidade não corresponder

# EntityFactory.py
import random

# !/usr/bin/python
# -*- coding: utf-8 -*-
from code.Backgound import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy, Enemy3  # Importa a classe Enemy3
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Level2Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Level3Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'level3Bg{i}', (0, 0)))
                    list_bg.append(Background(f'level3Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy3':  # Adiciona o case para o Enemy3
                return Enemy3('Enemy3', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))

# Game.py

#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.DOUBLEBUF)  # Corrigido
        self.clock = pygame.time.Clock()  # Controle de FPS

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level.run(self.clock)  # Passando o clock para controlar o FPS
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass

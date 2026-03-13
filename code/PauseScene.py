import pygame, sys
from settings import *
from buttons import Button

class PauseScene():
    def __init__(self, main, display, gameStateManager):
        self.main = main
        self.display = display
        self.gameStateManager = gameStateManager
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH), pygame.RESIZABLE)
        self.menu_font = pygame.font.Font(UI_FONT, 70)
        self.font = pygame.font.Font(UI_FONT, 40)
        
        
    def run(self):
        while True:
            self.screen.fill('pink')
        
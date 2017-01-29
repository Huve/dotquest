import pygame
import json
import sys

from pygame.locals import *

class CharacterCreationMenu():
    def __init__(self, screen, w, h):
        self.screen = screen
    def draw_dot(self):
        pass
    def run(self):
        """Runs the menu."""
        
        while 1:
            mos_x, mos_y = pygame.mouse.get_pos()
            self.screen.fill((255, 255, 255))
            #self.load_background("images/menu_background.png")
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit(); sys.exit()
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    pygame.quit(); sys.exit()
            pygame.display.update()

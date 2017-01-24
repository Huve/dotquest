import pygame
import random
import sys
import time

from dotquest_game import Game
from pygame.locals import *

class MainMenu():
    """The menu screen when starting the game."""
    def __init__(self, w, h):
        self.w = w
        self.h = h
        pygame.init()
        self.display = pygame.display
        self.screen = self.display.set_mode((w, h))
        
    def do_animations(self):
        """Animates all things on menu screen."""
        self.animate_bloop(700, 160, 50)
    
    def animate_bloop(self, x, y, max_size, color=(0, 162, 232)):
        """Animates the menu screen bloops."""
        half_size = int(max_size / 2)
        bloop_surface = pygame.Surface((max_size, max_size), pygame.SRCALPHA, 32)
        a_bloop = pygame.draw.circle(bloop_surface, color, (half_size, half_size), half_size)
        self.screen.blit(bloop_surface, (x, y))
        pygame.display.flip()

        
    def set_text(self):
        """Sets the menu text."""
        pass

    def load_background(self, image):
        """Loads the menu background image."""
        self.bg = pygame.image.load(image).convert()
        
    def load_game(self):
        """Loads the game with the character and server."""
        game = Game(self.w, self.h, self.screen)
        game.run()

    def select_character(self):
        """Selects a character for this session."""
        pass

    def select_server(self):
        """Selects a server for this session."""
        pass
        
    def display_screen(self):
        """Displays the menu screen."""
        self.screen.blit(self.bg, (0, 0))
        pygame.display.update()

    def play_menu_music(self):
        """Plays the menu music for dotquest."""
        pygame.mixer.init()
        pygame.mixer.music.load("audio/splort_2.mp3")
        pygame.mixer.music.play()

    def run(self):
        """Runs the menu."""
        self.load_background("images/menu.png")
        self.play_menu_music()
        self.display_screen()
        self.do_animations()
        
        while 1:
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit(); sys.exit()
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    pygame.quit(); sys.exit()
                if e.type == KEYDOWN and e.key == K_RETURN:
                    self.load_game()

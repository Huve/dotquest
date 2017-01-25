import pygame
import random
import sys

from dotquest_game import Game
from pygame.locals import *
from pygame import Rect

class MainMenu():
    """The menu screen when starting the game."""
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.timer = 0
        self.bloop_event = pygame.USEREVENT + 1
        self.bloops = {}
        pygame.init()
        self.display = pygame.display
        self.screen = self.display.set_mode((w, h))
        
    def do_animations(self):
        """Animates all things on menu screen."""
        pygame.time.set_timer(self.bloop_event, 30)
    
    def draw_bloop(self, x, y, max_size, color=(0, 162, 232)):
        """Animates the menu screen bloops."""
        a_bloop = pygame.draw.circle(self.screen, color, (x, y), int(max_size/2))
        self.bloops[len(self.bloops.keys())] = {
            "rect": a_bloop,
            "grow":True,
            "x": x,
            "y": y,
            "color": color,
            "max_size": max_size
            }

    def animate_bloops(self):
        for key in self.bloops.keys():
            r = self.bloops[key]['rect']
            c = self.bloops[key]['color']
            x = self.bloops[key]['x']
            y = self.bloops[key]['y']
            max_size = self.bloops[key]['max_size']
            if self.bloops[key]['grow'] == True: 
                r.inflate_ip(1, 1)
                self.bloops[key]['grow'] = r.width < max_size
            else: 
                r.inflate_ip(-1, -1)
                self.bloops[key]['grow'] = r.width < 5
            pygame.draw.circle(self.screen, c, (x, y), r.width)
            
    def set_text(self):
        """Sets the menu text."""
        pass

    def load_background(self, image):
        """Loads the menu background image."""
        self.bg = pygame.image.load(image).convert()
        self.screen.blit(self.bg, (0, 0))
        pygame.display.update()
   
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

    def play_menu_music(self):
        """Plays the menu music for dotquest."""
        pygame.mixer.init()
        pygame.mixer.music.load("audio/splort_2.mp3")
        pygame.mixer.music.play()

    def run(self):
        """Runs the menu."""
        self.load_background("images/menu.png")
        self.play_menu_music()
        self.draw_bloop(700, 160, 25)
        self.draw_bloop(220, 90, 18)
        self.draw_bloop(300, 480, 40)
        self.draw_bloop(1000, 660, 10)
        self.do_animations()
        
        while 1:
            self.screen.fill((255, 255, 255))
            self.load_background("images/menu.png")
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit(); sys.exit()
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    pygame.quit(); sys.exit()
                if e.type == KEYDOWN and e.key == K_RETURN:
                    self.load_game()
                if e.type == self.bloop_event:
                    self.animate_bloops()
            pygame.display.update()

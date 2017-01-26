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
        self.font = pygame.font.SysFont('Arial', 45)
        self.display = pygame.display
        self.screen = self.display.set_mode((w, h))
        
    def do_animations(self):
        """Animates all things on menu screen."""
        pygame.time.set_timer(self.bloop_event, 30)
    
    def draw_bloop(self, start_pos, final_pos, max_size, color=(208, 224, 227)):
        """Animates the menu screen bloops."""
        a_bloop = pygame.draw.circle(self.screen, color, (start_pos[0], start_pos[1]), int(max_size/2))
        self.bloops[len(self.bloops.keys())] = {
            "rect": a_bloop,
            "grow":True,
            "x": final_pos[0],
            "y": final_pos[1],
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
            x_adjust = 0
            y_adjust = 0
            # Adjust size:
            if self.bloops[key]['grow'] == True: 
                r.inflate_ip(1, 1)
                self.bloops[key]['grow'] = r.width < max_size
            else: 
                r.inflate_ip(-1, -1)
                self.bloops[key]['grow'] = r.width < 5
            # Move x, y:
            if self.bloops[key]['x'] < r.centerx:
                x_adjust = -1
            elif self.bloops[key]['x'] > r.centerx:
                x_adjust = 1
            if self.bloops[key]['y'] > r.centery:
                y_adjust = 1
            elif self.bloops[key]['y'] < r.centery:
                 y_adjust = -1
            r.move_ip(x_adjust, y_adjust)
            pygame.draw.circle(self.screen, c, (r.centerx, r.centery), r.width)
            
    def set_text(self, text, pos, color=(0, 0, 0)):
        """Sets the menu text."""
        label = self.font.render(text, 1, color)
        self.screen.blit(label, pos)

    def load_background(self, image):
        """Loads the menu background image."""
        self.bg = pygame.image.load(image).convert()
        self.screen.blit(self.bg, (0, 0))
   
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
        pygame.mixer.music.play(-1)

    def run(self):
        """Runs the menu."""
        start_ticks = pygame.time.get_ticks()
        self.play_menu_music()
        self.draw_bloop((300, 150), (450, 160), 25)
        self.draw_bloop((300, 150),(220, 40), 18)
        self.draw_bloop((300, 340),(300, 480), 40)
        self.draw_bloop((300, 340),(100, 420), 10)
        self.do_animations()
        
        
        while 1:
            seconds = (pygame.time.get_ticks()-start_ticks)/1000
            self.screen.fill((255, 255, 255))
            self.load_background("images/menu_background.png")
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit(); sys.exit()
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    pygame.quit(); sys.exit()
                if e.type == KEYDOWN and e.key == K_RETURN:
                    self.load_game()
                if e.type == self.bloop_event:
                    self.animate_bloops()
                if seconds > 7:
                    self.set_text("PRESS ENTER", (500, 500))
            pygame.display.update()

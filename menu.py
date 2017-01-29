import json
import pygame
import random
import sys

from dotquest_game import Game
from character_creation import CharacterCreationMenu
from pygame.locals import *
from pygame import Rect

class MenuDot():
    """A Dot to choose from on the home screen."""
    def __init__(self, menu, dot_id, dot_data, y):
        self.dot_data = dot_data
        self.dot_id = dot_id
        self.menu = menu
        self.y = y
        if dot_id != "0":
            self.color = self.get_color()
        self.screen = self.menu.screen
        self.font = pygame.font.SysFont('Roboto', 20)
        self.background_color = (220, 220, 220)
        self.highlight = (208, 224, 227)

    def choose(self):
        """Chooses this dot for play."""
        pass

    def test_mos_pos(self, x, y, width, height, mos_pos):
        """Detects if mos pos is in box."""
        mos_x, mos_y = mos_pos
        x_inside = False
        y_inside = False
        if mos_x > x and (mos_x < x + width):
            x_inside = True
        if mos_y > y and (mos_y < y + height):
            y_inside = True
        if x_inside and y_inside:
            return True
        else:
            return False
        
        
    def draw(self, mos_pos):
        """Draws one of the dots in the data"""
        x = 510
        y = 510 + 30 * self.y
        button_width = 200
        button_height = 30
        if self.test_mos_pos(x-15, y-15, button_width, button_height, mos_pos):
            button_color = self.highlight
            self.menu.selected_dot_id = self.dot_id
        else:
            if self.menu.selected_dot_id == self.dot_id:
                self.menu.selected_dot_id = None
            button_color = self.background_color
        pygame.draw.rect(self.screen, button_color, (x-15, y-15, button_width, button_height))
        if self.dot_id != "0":
            pygame.draw.circle(self.screen, self.color, (x, y), 10)
            dot_text = "%s (%s %s): %s" % (self.dot_data['name'],
                                            self.dot_data['level'],
                                            self.dot_data['player_class'],
                                            self.dot_data['last_biome'])
            label = self.font.render(dot_text, 1, (0, 0, 0))
        else:
            dot_text = "+ Create new Dot"
            label = self.font.render(dot_text, 1, (0, 0, 0))
        self.screen.blit(label, (x+20, y-6))
        
    def delete(self):
        """Deletes this dot permanently."""
        pass

    def get_color(self):
        class_color = {
            "tank": (255, 0, 0),
            "heal": (0, 255, 0),
            "deep": (0, 0, 255)
            }
        return class_color[self.dot_data['player_class']]
    
class MainMenu():
    """The menu screen when starting the game."""
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.timer = 0
        with open("data/characters.json", 'r') as database:
            self.all_dots = json.load(database)
        self.all_dots[0] = {}
        self.selected_dot_id = None
        self.menu_dots = []
        self.bloop_event = pygame.USEREVENT + 1
        self.bloops = {}
        pygame.init()
        self.font = pygame.font.SysFont('Roboto', 45)
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
            
    def draw_selections(self, x, y):
        count = 0
        for dot in self.all_dots.keys():
            if dot != 0:
                count += 1
                menudot = MenuDot(self, dot, self.all_dots[dot], count)
                self.menu_dots.append(menudot)
                menudot.draw((x, y))
        if count < 3:
            menudot = MenuDot(self, "0", {}, 3)
            self.menu_dots.append(menudot)
            menudot.draw((x, y))
        
    def set_text(self, text, pos, color=(0, 0, 0)):
        """Sets the menu text."""
        label = self.font.render(text, 1, color)
        self.screen.blit(label, pos)

    def load_background(self, image):
        """Loads the menu background image."""
        self.bg = pygame.image.load(image).convert()
        self.screen.blit(self.bg, (0, 0))
   
    def load_game(self, dot):
        """Loads the game with the character and server."""
        game = Game(self.w, self.h, self.screen, dot)
        game.run()

    def load_character_creation_menu(self):
        """Selects a character for this session."""
        char_creation_menu = CharacterCreationMenu(self.screen, self.w, self.h)
        char_creation_menu.run()

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
        self.set_text("PRESS ENTER", (500, 500))
        
        while 1:
            mos_x, mos_y = pygame.mouse.get_pos()
            seconds = (pygame.time.get_ticks()-start_ticks)/1000
            self.screen.fill((255, 255, 255))
            self.load_background("images/menu_background.png")
            selection = self.draw_selections(mos_x, mos_y)
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit(); sys.exit()
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    pygame.quit(); sys.exit()
                if e.type == self.bloop_event:
                    self.animate_bloops()
                if e.type == pygame.MOUSEBUTTONUP and self.selected_dot_id != "0":
                    self.load_game(self.selected_dot_id)
                if e.type == pygame.MOUSEBUTTONUP and self.selected_dot_id == "0":
                    self.load_character_creation_menu()
            pygame.display.update()

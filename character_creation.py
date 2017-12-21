import pygame
import json
import sys
import game_menu as m
import libraries.eztext as eztext

from dot import Dot
from dot_base import base_data

from pygame.locals import *

class CharacterDot():
    def __init__(self, menu, player_class, y):
        self.menu = menu
        self.player_class = player_class
        self.y = y
        self.color = self.get_color()
        self.screen = self.menu.screen
        self.font = pygame.font.SysFont('Roboto', 20)
        self.background_color = (220, 220, 220)
        self.highlight = (208, 224, 227)

    def draw(self, mos_pos):
        x = 510
        y = 310 + 30 * self.y
        button_width = 200
        button_height = 30
        if self.test_mos_pos(x-15, y-15, button_width, button_height, mos_pos):
            button_color = self.highlight
            self.menu.selected_class = self.player_class
        else:
            if self.menu.selected_class == self.player_class:
                self.menu.selected_class = None
            button_color = self.background_color
        pygame.draw.rect(self.screen, button_color, (x-15, y-15, button_width, button_height))
        pygame.draw.circle(self.screen, self.color, (x, y), 10)
        dot_text = "%s" % self.player_class
        label = self.font.render(dot_text, 1, (0, 0, 0))
        self.screen.blit(label, (x+20, y-6))
    
    def get_color(self):
        class_color = {
            "tank": (255, 0, 0),
            "heal": (0, 255, 0),
            "deep": (0, 0, 255),
            "denk": (150, 0, 150),
            "henk": (150, 150, 0),
            "heep": (0, 150, 150)
            }
        return class_color[self.player_class]
    
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
        
class CharacterCreationMenu():
    def __init__(self, screen, w, h):
        self.w = w
        self.h = h
        self.menu_dots = []
        self.screen = screen
        self.background_color = (220, 220, 220)
        self.highlight = (208, 224, 227)
        self.all_classes = list(base_data.keys())
        self.selected_class = None
        self.current_name = ""
        self.textbox = eztext.Input(y=300,maxlength=45, color=(0,105,92), prompt='First, name your dude: ')
        
    def draw_dot(self):
        pass

    def draw_options(self, x, y):
        count = 0
        for dot in self.all_classes:
            count += 1
            character_dot = CharacterDot(self, dot, count)
            self.menu_dots.append(character_dot)
            character_dot.draw((x, y))
            
    def run(self):
        """Runs the menu."""
        while 1:
            events = pygame.event.get()
            mos_x, mos_y = pygame.mouse.get_pos()
            self.screen.fill((255, 255, 255))
            self.draw_options(mos_x, mos_y)
            self.textbox.update(events)
            self.textbox.draw(self.screen)
            for e in events:
                if e.type == QUIT:
                    pygame.quit(); sys.exit()
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    pygame.quit(); sys.exit()
                if e.type == pygame.MOUSEBUTTONUP and self.selected_class and e.button == 1:
                    if self.textbox.value.strip() == "":
                        print("Name is empty. Enter a name.")
                    else:
                        dot = Dot()
                        dot.create_new(self.selected_class, self.textbox.value)
                        dot.save()
                        menu = m.MainMenu(self.w, self.h)
                        menu.run()
            pygame.display.update()

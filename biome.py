import csv
import math
import pygame
from player import Entity

class Block(Entity):
    """An entity that acts as a first layer (collision layer) tile on the map."""
    def __init__(self, a, x, y):
        Entity.__init__(self)
        self.image_map = {
        "T":"images/tree_2.png",
        "V":"images/bush_1.png",
        "R":"images/rock_1.png",
        "X":"images/bush_1.png",
        }
        self.image = pygame.Surface((64, 64))
        self.image = pygame.image.load(self.image_map[a])
        self.image.convert()
        self.rect = pygame.Rect(x, y, 64, 64)

    def update(self):
        pass

class Biome():
    """A biome in which players can journey."""
    def __init__(self, geography, screen, w=6400, h=6400):
        """Initializes the biome.

        Args:
          geography: type of biome in string, e.g., 'forest'
          w: width of biome.
          h: height of biome.
        """
        self.empty_tile = "-"
        self.w = w
        self.h = h
        self.tile_size = 64
        self.geography = geography
        self.screen = screen
        foreground_entities = "maps/" + geography + "_entities.tsv"
        self.foreground_data = []
        with open(foreground_entities, 'r') as f_e:
            reader = csv.reader(f_e, delimiter="\t")
            for row in reader:
                for tile in row:
                    self.foreground_data.append(tile)
        self.background_surface = pygame.Surface((self.w, self.h))
        self.draw_background()
        self.draw_foreground()

    def draw_background(self):
        """Draws the biome background color."""
        backgrounds = {
            "forest": (38, 106, 46),
            "desert": (194, 178, 128)
            }
        self.background_surface.fill(backgrounds[self.geography])
        
    def draw_foreground(self):
        """Draws the first layer (player level) of biome."""
        index = 0
        for tile in self.foreground_data:
            if tile != self.empty_tile:
                x_pos = (index * self.tile_size) % self.w
                y_pos = math.floor((index * self.tile_size) / self.w) * self.tile_size
                b = Block(tile, x_pos, y_pos)
                self.screen.entity_layer_1.add(b)
            index += 1

    def draw_overlay(self):
        """Draws the top layer of the biome."""
        pass


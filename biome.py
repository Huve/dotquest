import pygame
from player import Entity

class Block(Entity):
    """An entity that acts as a first layer (collision layer) tile on the map."""
    def __init__(self, a, x, y):
        Entity.__init__(self)
        self.image_map = {
        "tree":"images/tree_1.png",
        "bush":"images/bush_1.png",
        "rock":"images/bush_1.png",
        }
        self.image = pygame.image.load(self.image_map[a])
        self.image.convert()
        self.rect = pygame.Rect(x, y, 64, 64)

    def update(self):
        pass

class Biome():
    """A biome in which players can journey."""
    def __init__(self, geography, w=10000, h=10000):
        """Initializes the biome.

        Args:
          geography: type of biome in string, e.g., 'forest'
          w: width of biome.
          h: height of biome.
        """
        self.w = w
        self.h = h
        self.geography = geography
        self.background_surface = pygame.Surface((self.w, self.h))
        self.draw_background()

    def draw_background(self):
        """Draws the biome background color."""
        backgrounds = {
            "forest": (38, 106, 46)
            }
        self.background_surface.fill(backgrounds[self.geography])
        
    def draw_foreground(self):
        """Draws the first layer (player level) of biome."""
        foregrounds = {
            "forest": {
                "tree": 0,
                "bush": 0,
                "rock": 0
                }
            }
        self.foreground_densities = foregrounds[self.geography]

    def draw_overlay(self):
        """Draws the top layer of the biome."""
        pass


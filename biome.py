import pygame

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
        pass

    def draw_overlay(self):
        """Draws the top layer of the biome."""
        pass


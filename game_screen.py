#!/usr/bin/python
#
# April 3 2016
import camera
import pygame

from biome import Biome
from camera import simple_camera, complex_camera

class GameScreen():
    """Game Screen class that acts as a view for the user"""
    def __init__(self, game, screen, player, biome, w, h):
        self.tile_size = 64
        self.w = w
        self.h = h
        self.game = game
        self.screen = screen
        self.entity_layer_1 = pygame.sprite.Group()
        self.biome = Biome(biome, self)
        self.player = player
        #self.entity_layer_2 = pygame.sprite.Group()
        #self.screen = display.set_mode((w, h))
        self.total_width = self.biome.w
        self.total_height = self.biome.h
        self.camera = camera.Camera(complex_camera, self.total_width, self.total_height)
        self.player.draw_player()
        self.draw_layers()
        pygame.display.flip()
    
    def draw_layers(self):
        self.camera.update(self.player)
        self.screen.blit(self.biome.background_surface, (self.camera.state[0], self.camera.state[1]))
        self.screen.blit(self.player.surface, self.camera.apply(self.player))
        for e in self.entity_layer_1:
           e.update()
           self.screen.blit(e.image, self.camera.apply(e))
        #self.screen.blit(self.ui.layer, (0, 0))
        pygame.display.update()
         
    def animate_sprite(self, sprite, image):
        pass

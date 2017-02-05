import game_screen
import player
import pygame
import sys

from pygame.locals import *

class Game():
    """Game class that stores what is occurring during the game."""
    def __init__(self, w, h, display, dot_id):
        """Initializes the game.

        Args:
          w: width of the game screen.
          h: height of the game screen.
        """
        self.player = player.Player(dot_id)
        self.biome = self.player.data["last_biome"]
        self.display = display
        self.screen = game_screen.GameScreen(self, self.display, self.player, self.biome, w, h)
        self.clock = pygame.time.Clock()
        self.clock.tick(30)
        self.up = False
        self.right = False
        self.down = False
        self.left = False
        self.right = False
        self.running = False
        self.direction = None
        self.current_press = None
        self.layer_1 = self.screen.entity_layer_1
       # self.layer_2 = self.screen.entity_layer_2
        if not pygame.mixer:
            print('NO MIXER')
            pygame.mixer.init()
        pygame.mixer.music.load("audio/splort_4.mp3")
        pygame.mixer.music.play()

    def run(self):
        """Runs the game."""
        while 1:
            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                self.direction = "left"
                self.player.update(self.direction, self.layer_1)
            if keys[K_a]:
                self.direction = "left"
                self.player.update(self.direction, self.layer_1)
            if keys[K_RIGHT] or keys[K_d]:
                self.direction = "right"
                self.player.update(self.direction, self.layer_1)
            if keys[K_UP] or keys[K_w]:
                self.direction = "up"
                self.player.update(self.direction, self.layer_1)
            if keys[K_DOWN] or keys[K_s]:
                self.direction = "down"
                self.player.update(self.direction, self.layer_1)
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit(); sys.exit()
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    pygame.quit(); sys.exit()
                if e.type == KEYDOWN and e.key == K_SPACE:
                    self.running = True
                if e.type == KEYUP:
                    if e.key == K_UP or e.key == K_DOWN or e.key == K_LEFT or e.key == K_RIGHT or e.key == K_d or e.key == K_a or e.key == K_w or e.key == K_s:
                        self.direction = None
            self.player.update(self.direction, self.layer_1)
            self.screen.draw_layers() 


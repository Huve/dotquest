#!/usr/bin/python
#
# April 3 2016
import pygame

class Entity(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        
class Player(Entity):
    """Player class Entity."""
    def __init__(self):
        Entity.__init__(self)
        self.load_player_data()
        self.rect = pygame.Rect(self.x, self.y, 32, 64)


    def get_color(self):
        class_color = {
            "tank": (255, 0, 0),
            "heal": (0, 255, 0),
            "deep": (0, 0, 255)
            }
        return class_color[self.player_class]
        
        
    def update(self, direction, layer_1):
        """Update the player's position.
        
        Args:
            up: boolean referring to keypress up.
            down: boolean referring to keypress down.
            left: boolean referring to keypress left.
            right: boolean referring to keypress right.
            running: boolean referring to spacebar press.
            layer_1: list of sprites that player can collide with.
        """
        if direction == "up":
            self.yvel = -2
            self.xvel = 0
        if direction == "down":
            self.yvel = 2
            self.xvel = 0
        if direction == "left":
            self.xvel = -2
            self.yvel = 0
        if direction == "right":
            self.xvel = 2
            self.yvel = 0
        if direction not in ("right", "left", "up", "down"):
            self.xvel = 0
            self.yvel = 0
        self.rect.left += self.xvel
        self.rect.top += self.yvel
        self.collide(self.xvel, 0, layer_1)
        self.collide(0, self.yvel, layer_1)

        
    def collide(self, xvel, yvel, layer_1):
        """Determine if player is colliding with objects
        
        Args:
            xvel: speed on x axis.
            yvel: speed on y axis.
            layer_1: list of sprites that player can collide with.
        """
        for p in layer_1:
            if pygame.sprite.collide_rect(self, p):
               # if isinstance(p, GroundBlock):
                   # pass  # TODO(huve): add doors to this ExitBlock
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                if yvel < 0:
                    self.rect.top = p.rect.bottom

            
    def draw_player(self):
        self.surface = pygame.Surface((self.level * 2, self.level * 2), pygame.SRCALPHA, 32)
        self.graphic = pygame.draw.circle(self.surface, self.color, (self.level, self.level), self.level)

    def load_player_data(self):
        # TODO: load from database
        self.last_biome = "forest"
        self.player_class = "tank"
        self.name = "Dlob"
        self.x = 500
        self.y = 500
        self.level = 10
        self.health = 10
        self.mana = 10
        self.strength = 10
        self.intelligence = 10
        self.dexterity = 10
        self.color = self.get_color()

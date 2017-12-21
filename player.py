#!/usr/bin/python
#
# April 3 2016
import pygame
import json  # change when moving to sqlite

from abilities import class_abilities
from game_entity import Entity

        
class Player(Entity):
    """Player class Entity."""
    def __init__(self, pid):
        Entity.__init__(self)
        self.color = None
        self.data = {}
        self.load_player_data(pid)
        self.rect = pygame.Rect(self.data['x'],
                                self.data['y'],
                                2 * self.data['level'] + 20,
                                2 * self.data['level'] + 20)
        self.player_class = self.data['player_class']
        self.left_click_ability = class_abilities[self.player_class][0]

    def get_color(self):
        class_color = {
            "tank": (255, 0, 0),
            "heal": (0, 255, 0),
            "deep": (0, 0, 255),
            "denk": (150, 0, 150),
            "henk": (150, 150, 0),
            "heep": (0, 150, 150)
            }
        return class_color[self.data['player_class']]
        
    def update(self, direction, layer_1):
        """Update the player's position.
        
        Args:
            direction: the direction the player is running.
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
                    # pass TODO(huve): add doors to this ExitBlock
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                if yvel < 0:
                    self.rect.top = p.rect.bottom

    def use_ability(self, screen, coords):
        """Uses the left click ability"""
        player_screen_x = self.rect.centerx + screen.camera.state.left
        player_screen_y = self.rect.centery + screen.camera.state.top
        self.left_click_ability.do_ability(screen, coords, (player_screen_x, player_screen_y))

    def draw_player(self):
        level = self.data["level"]
        width = 2 * level + 20
        half_width = int(width / 2)
        self.surface = pygame.Surface((width, width), pygame.SRCALPHA, 32)
        self.graphic = pygame.draw.circle(self.surface, self.color, (half_width, half_width), half_width)

    def load_player_data(self, player_id):
        with open("data/characters.json", 'r') as database:
            j = json.load(database)
            self.data = j[player_id]
            print("loaded player: %s" % self.data)
        self.color = self.get_color()

    def save(self):
        pass

def main():
    pid = "1"
    player = Player(pid)
        
if __name__ == "__main__":
    main()

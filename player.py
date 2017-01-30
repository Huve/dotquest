#!/usr/bin/python
#
# April 3 2016
import pygame
import json # change when moving to sqlite
import glob # change when moving to sqlite

class Entity(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        
class Player(Entity):
    """Player class Entity."""
    def __init__(self, pid):
        Entity.__init__(self)
        self.load_player_data(pid)
        self.rect = pygame.Rect(self.data['x'], self.data['y'], 5, 5)

    def get_color(self):
        class_color = {
            "tank": (255, 0, 0),
            "heal": (0, 255, 0),
            "deep": (0, 0, 255)
            }
        return class_color[self.data['player_class']]
        
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
        level = self.data["level"]
        self.surface = pygame.Surface((level * 2, level * 2), pygame.SRCALPHA, 32)
        self.graphic = pygame.draw.circle(self.surface, self.color, (level, level), level)

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

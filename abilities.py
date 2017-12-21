import math
import pygame

from game_entity import Entity


class Ability(Entity):
    def __init__(self):
        """Initializes."""
        Entity.__init__(self)
        self.screen = None
        self.player_coords = None
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.maximum_range = None
        self.rect = None

    def do_ability(self, player_coords):
        pass

    def collide(self):
        pass


class BasicAttack(Ability):
    def __init__(self):
        Ability.__init__(self)

    def do_ability(self, screen, coords, player_coords):
        self.screen = screen
        self.player_coords = player_coords
        # TODO FINISH THE MATH HERE
        self.maximum_range = 64
        self.height = 64
        self.width = 64
        slope = (coords[1] - player_coords[1]) / (coords[0] - player_coords[0])
        angle = math.degrees(math.atan(-slope))
        self.x = player_coords[0] + self.maximum_range * math.cos(angle)
        self.y = player_coords[1] + self.maximum_range * math.sin(angle)
        print(player_coords, coords, self.x, self.y, angle)
        self.image = pygame.Surface((64, 64))
        self.rect = pygame.Rect(self.x, self.y, 64, 64)
        #self.image =
        screen.entity_layer_1.add(self)
        #pygame.draw.rect(screen.screen, (0, 0, 0), (100, 100, 100, 100))

basic_attack = BasicAttack()

class_abilities = {
    "tank": [basic_attack],
   # "deep": [Ability.basic_melee, Ability.basic_ranged],
   # "heal": [Ability.basic_ranged],
   # "henk": [Ability.basic_melee],
   # "heep": [Ability.basic_melee, Ability.basic_ranged],
   # "denk": [Ability.basic_melee]
}
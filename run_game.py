#!/usr/bin/python
#
# Jan 22 2016

import dotquest_game

WIDTH = 1028
HEIGHT = 768

HALF_WIDTH = WIDTH/2
HALF_HEIGHT = HEIGHT/2

if __name__ == "__main__":
    game = dotquest_game.Game(WIDTH, HEIGHT)
    game.run()

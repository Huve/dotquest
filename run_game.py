#!/usr/bin/python
#
# Jan 22 2016

from game_menu import *

WIDTH = 1024
HEIGHT = 768

HALF_WIDTH = WIDTH/2
HALF_HEIGHT = HEIGHT/2

if __name__ == "__main__":
    menu = MainMenu(WIDTH, HEIGHT)
    menu.run()

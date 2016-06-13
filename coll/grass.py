import random

from pico2d import *

class Grass:
    def __init__(self):

        self.image = load_image('grass.png')
        self.x = 400
        self.y = 30

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x-400, self.y-30, self.x+400, self.y+30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


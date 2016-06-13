import random
import json
import os


from pico2d import *
from hero_controller import Hero

import game_framework
import title_state



name = "MainState"

boy = None
grass = None

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

def enter():
    global hero, grass
    hero = Hero()
    grass = Grass()
    pass


def exit():
    global  hero, grass
    del(hero)
    del(grass)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        hero.handle_event(event)


def update():
    global hero
    hero.update()
    pass


def draw():
    clear_canvas()
    grass.draw()
    hero.draw()
    delay(0.04)
    update_canvas()
    pass





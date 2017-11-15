from background import Background

import game_framework
import main_state
from My_pico2d import *

name = "StartState"
bgm = None
background = None

#frames = 0
#Timer = SDL_GetTicks()

def enter():
    delay(3)
    global background

    background = Background()

def exit():
    global background, bgm
    del(background)
    del(bgm)

def update():

    background.update()


def draw():
    clear_canvas()

    background.draw()

    update_canvas()



def pause(): pass


def resume(): pass

def handle_events():
    events = get_events()
    for event in events:
        if (event.type == SDL_QUIT) or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            game_framework.quit()

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE) or (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN) :
            game_framework.change_state(main_state)



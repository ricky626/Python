import game_framework

from My_pico2d import *

from hero import Hero

name = "MainState"
hero = None

#frames = 0
#Timer = SDL_GetTicks()

def enter():
    global hero

    hero = Hero()
    pass


def exit():
    global hero
    del(hero)

    pass

def update():
    hero.update()
    pass


def draw():
    clear_canvas()

    hero.draw()

    update_canvas()



def pause(): pass


def resume(): pass

def handle_events():
    events = get_events()
    for event in events:
        if (event.type == SDL_QUIT) or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            game_framework.quit()

        hero.handle_events(event)
        #elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE) or (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN) :
            #game_framework.change_state(main_state)



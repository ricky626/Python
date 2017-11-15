import game_framework
from My_pico2d import *
from logo import Logo

name = "LogoState"

logo = None

def enter():
    global logo
    open_canvas(1024, 768)
    hide_lattice()

    logo = Logo()

def exit():
    global logo
    del(logo)

def update():
    logo.update()
    pass

def draw():
    clear_canvas()

    logo.draw()

    update_canvas()


def pause(): pass


def resume(): pass

def handle_events():
    events = get_events()
    for event in events:
        if (event.type == SDL_QUIT) or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            game_framework.quit()

        #elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE) or (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN) :
         #   game_framework.change_state(main_state)



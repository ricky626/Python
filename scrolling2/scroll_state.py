from pico2d import *

import game_framework


from boy import FreeBoy as Boy # import Boy class from boy.py
from background import FixedBackground as Background
from ball import Ball

name = "scroll_state"

count = 100
boy = None
balls = None
background = None


def create_world():
    global boy, background, balls
    boy = Boy()
    background = Background()
    balls = [Ball() for i in range(100)]

    background.set_center_object(boy)
    boy.set_background(background)

    for ball in balls:
        ball.set_background(background)

def destroy_world():
    global boy, background, balls
    del(balls)
    del(boy)
    del(background)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    open_canvas(800, 600)
    hide_cursor()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                boy.handle_event(event)
                background.handle_event(event)



def update(frame_time):
    global count
    boy.update(frame_time)

    for ball in balls:
        if collide(boy, ball):
            balls.remove(ball)
            boy.eat(ball)
            count -= 1

    for ball in balls:
        ball.update(frame_time)

    background.update(frame_time)



def draw(frame_time):
    clear_canvas()
    background.draw()
    for ball in balls:
        ball.draw()
    boy.draw()
    debug_print("ball : %d" % count)

    update_canvas()







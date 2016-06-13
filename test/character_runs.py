from idlelib.SearchEngine import get
from pico2d import *
import math
import cmath

open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

x = 400
frame = 0
r = 200
i = 0

while(1):

    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, r * math.cos(i)+400, r * math.sin(i) + 300)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.05)
    get_events()
    i-= 0.1

close_canvas()
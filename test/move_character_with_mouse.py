from pico2d import *

def handle_events():
    global running
    global x, y
    global r
    events = get_events()

    for event in events:
        if (event.type == SDL_QUIT) or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 599 - event.y


open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')



running = True
x, y = 100, 100
r = 100
frame = 0
i = 0
show_cursor()

while (running):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, r * math.cos(i) + x, r * math.sin(i) + y)
    update_canvas()
    frame = (frame + 1) % 8
    i-=0.3
    delay(0.05)
    handle_events()

close_canvas()





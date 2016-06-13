from pico2d import *

def handle_events():
    global running
    global x
    global y
    global r
    events = get_events()

    for event in events:
        if (event.type == SDL_QUIT) or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x+=10
            elif event.key == SDLK_LEFT:
                x-=10
            elif event.key == SDLK_UP:
                y+=10
            elif event.key == SDLK_DOWN:
                y-=10
            elif event.key == SDLK_a and r < 300:
                r+=10
            elif event.key == SDLK_d and r > 20:
                r-=10


open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

running = True
x = 400
y = 300
frame = 0
r = 100
i = 0

while (running):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, r * math.cos(i) + x, r * math.sin(i) + y)
    i-=0.5
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.05)
    handle_events()

close_canvas()


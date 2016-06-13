from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(300, 500), 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.moveX = random.randint(3, 10)
        self.MaxX = random.randint(10, 300)
        self.MaxX2 = random.randint(400, 800)

    def update(self):
        self.frame = random.randint(0, 7)
        #self.frame = (self.frame + 1) % 8
        if self.x >= self.MaxX2 or self.x <= self.MaxX:
            self.moveX *= -1
        self.x += self.moveX

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    global check

    events = get_events()
    for event in events:
        if (event.type == SDL_QUIT) or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                check = 1
            elif event.key == SDLK_LEFT:
                check = 2

        elif event.type == SDL_KEYUP:
            check = 0


open_canvas()

##team = [Boy()] * 11
team = [Boy() for i in range(11)]

grass = Grass()


running = True

check = 0

while (running):
    handle_events()


    clear_canvas()

    grass.draw()

    for boy in team:
        boy.update()
        boy.draw()

    update_canvas()

    delay(0.05)
    #if check == 1:
    #   boy.x += 10
    #elif check == 2:
    #    boy.x -= 10




close_canvas()


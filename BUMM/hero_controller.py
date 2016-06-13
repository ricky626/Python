# hero_controller.py : control hero move with left and right key

import random
from pico2d import *

running = None
hero = None

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Hero:
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3


    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.state = self.RIGHT_STAND
        self.rightbutton = False
        self.leftbutton = False
        if Hero.image == None:
            Hero.image = load_image('animation_sheet.png')

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                self.leftbutton = True
                pass

            if event.key == SDLK_RIGHT:
                self.rightbutton = True
                pass

        elif(event.type == SDL_KEYUP):
            if(event.key == SDLK_LEFT):
                self.leftbutton = False
            if(event.key == SDLK_RIGHT):
                self.rightbutton = False
        pass


    def update(self):


        if(self.leftbutton == True):
            self.state = self.LEFT_RUN
            self.x = max(0, self.x - 5)

        elif(self.leftbutton == False):
            if self.state == self.LEFT_RUN:
                self.state = self.LEFT_STAND

        if(self.rightbutton == True):
            self.x = min(800, self.x + 5)

            self.state = self.RIGHT_RUN

        elif(self.rightbutton == False):
            if self.state == self.RIGHT_RUN:
                self.state = self.RIGHT_STAND

        self.frame = (self.frame + 1) % 8

        pass

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)



def main():

    open_canvas()

    global hero
    global running

    hero = Hero()
    grass = Grass()

    running = True
    while running:

        hero.update()

        clear_canvas()
        grass.draw()
        hero.draw()
        update_canvas()

        delay(0.015)

    close_canvas()


if __name__ == '__main__':
    main()
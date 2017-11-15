import game_framework
import start_state
from My_pico2d import *


class Logo:
    image                         = [None for j in range(0, 84)]

    def __init__(self):

        self.logo_str = "res/logo/-.png"
        self.frames = 0

        if(Logo.image[0] == None):

            for i in range(0, 84):

                Logo.image[i] = load_image(self.logo_str.replace('-', str(i + 1)))


            self.Timer = SDL_GetTicks()





        pass

    def update(self):

        if(SDL_GetTicks() - self.Timer > 50):
            if(self.frames < 83):
                self.frames += 1
                self.Timer = SDL_GetTicks()

        if(self.frames == 83):
            game_framework.change_state(start_state)

        pass

    def draw(self):

        self.image[self.frames].draw(0, 0)

        pass
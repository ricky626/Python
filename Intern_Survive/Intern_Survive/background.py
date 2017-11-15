import random



from My_pico2d import *

name                                = "Background"


class Background:
    background                      = None


    def __init__(self):

        self.screenSizeX            = 1024
        self.screenSizeY            = 768
        self.rect                   = "res/mascot/-.png"

        self.moveTime               = SDL_GetTicks()
        self.PolygonDegree          = 0
        self.PolygonX               = [0 for j in range(0, 18)]
        self.PolygonY               = [0 for j in range(0, 18)]
        self.moveX                  = [0 for j in range(0, 18)]
        self.moveY                  = [0 for j in range(0, 18)]

        self.PolygonDegree          = [float(0) for i in range(0, 18)]
        self.degree                 = [float(0) for i in range(0, 18)]

        self.Polygon = [None for j in range(0, 18)]

        self.title = [None for j in range(0, 2)]
        self.frames = 0
        self.Timer = SDL_GetTicks()

        for i in range(0, 18):
            #self.PolygonX[i][j], self.PolygonY[i][j]    = random.randint(-self.ScreenSizeX/2, self.ScreenSizeX + 500), random.randint(-self.ScreenSizeY/2, self.ScreenSizeY + 500)
            self.PolygonX[i], self.PolygonY[i] = self.screenSizeX/2-140, self.screenSizeY/2-130
            self.moveX[i], self.moveY[i] = random.randint(-4, 4), random.randint(-4, 4)



        if(Background.background == None):
            Background.background = load_image("res/background.png")

            for i in range(0, 9):
                self.Polygon[i] = load_image(self.rect.replace('-', str(i + 1)))
                self.degree[i] = 0.02
                self.PolygonDegree[i] = 0.02

            for i in range(9, 18):
                self.Polygon[i] = load_image(self.rect.replace('-', str(i - 8)))
                self.degree[i] = -0.02
                self.PolygonDegree[i] = -0.02

            self.title[0] = load_image("res/menu/title1.png")
            self.title[1] = load_image("res/menu/title2.png")

            self.name = load_image("res/menu/name.png")

            self.star = load_image("res/menu/star.png")

            self.menu_sound = load_wav("res/menu/sound/menu.wav")
            self.menu_sound.set_volume(64)
            self.menu_sound.repeat_play()



        pass

    def update(self):
        for i in range(0, 18):
            if(self.PolygonX[i] > self.screenSizeX+200 or self.PolygonX[i] < -self.screenSizeX+400):
                self.moveX[i] *= -1
            elif(self.PolygonY[i] > self.screenSizeY+200 or self.PolygonY[i] < -self.screenSizeY+400):
                self.moveY[i] *= -1

            self.PolygonX[i] += self.moveX[i]
            self.PolygonY[i] += self.moveY[i]

            self.PolygonDegree[i] += self.degree[i]

        if (SDL_GetTicks() - self.Timer > 500):
            self.frames = (self.frames + 1) % 2
            self.Timer = SDL_GetTicks()

        pass

    def draw(self):
        self.background.draw(0, 0)

        for i in range(0, 18):
            self.Polygon[i].rotate_draw(self.PolygonDegree[i], self.PolygonX[i], self.PolygonY[i])

        self.title[self.frames].draw(150, 50)

        self.star.draw(75, 14)

        self.name.draw(620, 364)
        pass
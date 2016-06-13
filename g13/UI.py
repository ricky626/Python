__author__ = 'user'
from pico2d import *

class UI:
    def __init__(self):
        self.score = 0
        self.font = load_font("ConsolaMalgun.ttf", 40)

    def update(self, frame_time):
        self.time = get_time()
        pass

    def draw(self):
        print("score %d time %f" % (self.score, get_time()))
        self.font.draw(300, 550, 'Score %d Time %f' % (self.score, get_time()))
        self.time = 0


def test_ui():
    open_canvas()

    ui = UI()
    for i in range(100):

        ui.score = i
        ui.update(0)
        clear_canvas()
        ui.draw()

        update_canvas()
        delay(0.01)


    close_canvas()



if __name__ == '__main__':
    test_ui()






























__author__ = 'user'
from pico2d import *

class TUI:
    def __init__(self):
        self.font = load_font("ConsolaMalgun.ttf", 40)
        pass
    def draw(self):

        pass



def test_tui():
    open_canvas()

    tui = TUI()
    tui.draw()


    close_canvas()



if __name__ == '__main__':
    test_tui()






























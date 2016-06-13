import random

from pico2d import *


class FreeBoy:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 80.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    print(RUN_SPEED_PPS)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 1700, 300
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.xdir = 0
        self.ydir = 0
        self.state = self.RIGHT_STAND
        if FreeBoy.image == None:
            FreeBoy.image = load_image('animation_sheet.png')


    def set_background(self, bg):
        self.bg = bg


    def update(self, frame_time):
        self.life_time += frame_time
        distance = FreeBoy.RUN_SPEED_PPS * frame_time
        self.total_frames += FreeBoy.FRAMES_PER_ACTION * FreeBoy.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8
        self.x += (self.xdir * distance)
        self.y += (self.ydir * distance)

        self.x = clamp(0, self.x, self.bg.w)
        self.y = clamp(0, self.y, self.bg.h)


        if self.xdir == -1: self.state = self.LEFT_RUN
        elif self.xdir == 1: self.state = self.RIGHT_RUN
        elif self.xdir == 0:
            if self.state == self.RIGHT_RUN: self.state = self.RIGHT_STAND
            elif self.state == self.LEFT_RUN: self.state = self.LEFT_STAND


    def draw(self):
        # x_left_offset = min(0, self.x - self.canvas_width//2)
        # x_right_offset = max(0, self.x - self.bg.w + self.canvas_width//2)
        # x_offset = x_left_offset + x_right_offset
        # self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.canvas_width//2+x_offset, self.canvas_height//2)
        # debug_print('x=%d, y=%d, x_left_offset=%d, x_right_offset=%d' % (self.x, self.y, x_left_offset, x_right_offset))

        # x, y : map coord
        # sx, sy : screen coord
        # screen_origin_x : map coord x of screen_origin
        # screen_origin_y : map coord y of screen_origin
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        debug_print('x=%d, y=%d, sx=%d, sy=%d' % (self.x, self.y, sx, sy))

        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, sx, sy)



    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT: self.xdir += -1
            elif event.key == SDLK_RIGHT: self.xdir += 1
            elif event.key == SDLK_UP: self.ydir += 1
            elif event.key == SDLK_DOWN: self.ydir -= 1

        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT: self.xdir += 1
            elif event.key == SDLK_RIGHT: self.xdir += -1
            elif event.key == SDLK_UP: self.ydir -= 1
            elif event.key == SDLK_DOWN: self.ydir += 1

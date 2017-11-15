import game_framework
from My_pico2d import *


class Hero:
    background = [None for j in range(0, 10)]
    scene_name = [None for j in range(0, 10)]
    thanks = [None for j in range(0, 2)]
    qa = [None for j in range(0, 10)] # 문제 개수

    def __init__(self):


        self.frames = 0
        self.Scene_number = 0

        self.LeftButton = False
        self.RightButton = False
        self.JumpButton = True

        self.HeroX = 5
        self.HeroY = 472

        self.DropSpeed = 1
        self.JumpTime = -1

        self.switch_state = [False for j in range(0, 3)] # 스위치 상태
        self.switch_X = [False for j in range(0, 3)]  # 스위치 상태
        self.switch_Y = [False for j in range(0, 3)]  # 스위치 상태

        self.correct_list = [0 for i in range(0, 10)] # 정답
        self.correct_list[0] = 3
        self.correct_list[1] = 2
        self.correct_list[2] = 3
        self.correct_list[3] = 3
        self.correct_list[4] = 2

        self.correct_list[5] = 3
        self.correct_list[6] = 2
        self.correct_list[7] = 3
        self.correct_list[8] = 3
        self.correct_list[9] = 2

        self.clearView = False

        self.isCorrect = 0  # 아무것도 아닐때 0 # 맞으면 1 # 틀리면 2
        self.answer = 0

        self.clearTimer = 0

        self.backgroundX = 0
        self.backgroundY = 0
        self.menu_barX = 0
        self.menu_barY = 562
        self.scene_barX = 320
        self.scene_barY = 30
        self.scene_nameX = 320
        self.scene_nameY = 30
        self.qaX = 0
        self.qaY = 0
        self.thanks_Timer = 0

        self.ending_Timer = 0


        for i in range(0, 3):
            self.switch_X[i] = 300 + (250 * i)
            self.switch_Y[i] = 518


        if(Hero.background[0] == None):

            Hero.background[0] = load_image("res/game/map/map1.png")
            Hero.background[1] = Hero.background[0]
            Hero.background[2] = Hero.background[0]
            Hero.background[3] = load_image("res/game/map/map2.png")
            Hero.background[4] = load_image("res/game/map/map3.png")
            Hero.background[5] = load_image("res/game/map/map4.png")
            Hero.background[6] = Hero.background[3]
            Hero.background[7] = load_image("res/game/map/map5.png")
            Hero.background[8] = Hero.background[7]
            Hero.background[9] = Hero.background[0]


            Hero.menu_bar = load_image("res/game/map/menu_bar.png")

            Hero.scene_bar = load_image("res/game/map/scene_bar.png")


            Hero.scene_name[0] = load_image("res/game/map/scene_name/scene_name1.png")
            Hero.scene_name[1] = Hero.scene_name[0]
            Hero.scene_name[2] = Hero.scene_name[0]
            Hero.scene_name[3] = load_image("res/game/map/scene_name/scene_name2.png")
            Hero.scene_name[4] = load_image("res/game/map/scene_name/scene_name3.png")
            Hero.scene_name[5] = load_image("res/game/map/scene_name/scene_name4.png")
            Hero.scene_name[6] = Hero.scene_name[5]
            Hero.scene_name[7] = load_image("res/game/map/scene_name/scene_name5.png")
            Hero.scene_name[8] = Hero.scene_name[7]
            Hero.scene_name[9] = load_image("res/game/map/scene_name/scene_name6.png")

            Hero.qa[0] = load_image("res/game/map/qa/qa1.png")
            Hero.qa[1] = load_image("res/game/map/qa/qa2.png")
            Hero.qa[2] = load_image("res/game/map/qa/qa3.png")
            Hero.qa[3] = load_image("res/game/map/qa/qa4.png")
            Hero.qa[4] = load_image("res/game/map/qa/qa5.png")
            Hero.qa[5] = load_image("res/game/map/qa/qa6.png")
            Hero.qa[6] = load_image("res/game/map/qa/qa7.png")
            Hero.qa[7] = load_image("res/game/map/qa/qa8.png")
            Hero.qa[8] = load_image("res/game/map/qa/qa9.png")
            Hero.qa[9] = load_image("res/game/map/qa/qa10.png")

            Hero.hero = load_image("res/game/hero.png")

            Hero.switch_on = load_image("res/game/btn_on.png")
            Hero.switch_off = load_image("res/game/btn_off.png")

            Hero.correct = load_image("res/game/correct.png")
            Hero.fail = load_image("res/game/fail.png")

            Hero.clear_sound = load_wav("res/game/sound/clear.wav")
            Hero.clear_sound.set_volume(80)

            Hero.reset_sound = load_wav("res/game/sound/reset.wav")
            Hero.reset_sound.set_volume(40)

            Hero.jump_sound = load_wav("res/game/sound/jump.wav")
            Hero.jump_sound.set_volume(40)

            Hero.switch_sound = load_wav("res/game/sound/switch.wav")
            Hero.switch_sound.set_volume(40)

            Hero.main_sound = load_music("res/game/sound/main.mp3")
            Hero.main_sound.set_volume(64)
            Hero.main_sound.repeat_play()

            Hero.ending = load_image("res/game/ending/ending.png")
            Hero.end1 = load_image("res/game/ending/1.png")
            Hero.end2 = load_image("res/game/ending/2.png")
            Hero.end3 = load_image("res/game/ending/3.png")

            Hero.thanks[0] = load_image("res/game/ending/4.png")
            Hero.thanks[1] = load_image("res/game/ending/5.png")
            self.thanks_frames = 0

            Hero.name = load_image("res/game/ending/name.png")
            Hero.star = load_image("res/game/ending/thankstar.png")

            Hero.end_sound = load_music("res/game/sound/end.mp3")


        pass

    def update(self):

        if(self.Scene_number < 10):
            self.hero_move()
            self.hero_switch()

            if(self.isCorrect != 0):

                if(self.Scene_number < 9):
                    if(self.isCorrect == 1):
                        if(self.answer == 2):
                            self.HeroX -= 2.8
                        elif(self.answer == 3):
                            self.HeroX -= 4.0

                        self.map_move()


                if(SDL_GetTicks() - self.clearTimer > 3000):

                    if(self.isCorrect == 1):
                        if(self.Scene_number < 10):
                            self.Scene_number += 1

                        if(self.Scene_number == 10):
                            self.ending_Timer = SDL_GetTicks()

                        self.backgroundX = 0
                        self.menu_barX = 0
                        self.scene_barX = 320
                        self.scene_nameX = 320
                        self.qaX = 0
                        for i in range(0, 3):
                            self.switch_X[i] = 300 + (250 * i)

                    elif(self.isCorrect == 2):
                        self.HeroX = 5
                        self.HeroY = 472


                    self.scene_change()

        elif(self.Scene_number >= 10 and self.Scene_number < 13):
            if(SDL_GetTicks() - self.ending_Timer > 5000):
                self.Scene_number += 1
                self.ending_Timer = SDL_GetTicks()

        elif(self.Scene_number == 13):
            if (SDL_GetTicks() - self.thanks_Timer > 500):
                self.thanks_frames = (self.thanks_frames + 1) % 2
                self.thanks_Timer = SDL_GetTicks()

        pass

    def draw(self):
        if(self.Scene_number < 10):
            self.map_draw(self.Scene_number)

            if(self.isCorrect == 1):
                self.correct.draw(310, 130)
            elif(self.isCorrect == 2):
                self.fail.draw(310, 130)

        else:
            for i in range(10, 14):
                self.ending.draw(0, 0)

            if(self.Scene_number == 10):
                self.end1.draw(0, 0)
            elif(self.Scene_number == 11):
                self.end2.draw(0, 0)
            elif(self.Scene_number == 12):
                self.end3.draw(0, 0)
            elif(self.Scene_number == 13):
                self.thanks[self.thanks_frames].draw(0, 0)
                self.name.draw(120, 442)
                self.star.draw(200, 260)

        pass


    def handle_events(self, event):
        if(event.type == SDL_KEYDOWN):

            if(event.key == SDLK_LEFT):
                self.LeftButton = True

            if(event.key == SDLK_RIGHT):
                self.RightButton = True

            if(event.key == SDLK_1 and self.Scene_number > 0):
                self.scene_change()
                self.Scene_number -= 1

            elif (event.key == SDLK_2 and self.Scene_number < 13):
                self.scene_change()
                self.Scene_number += 1



        elif(event.type == SDL_KEYUP):
            if(self.LeftButton == True and event.key == SDLK_LEFT):
                self.LeftButton = False
            if (self.RightButton == True and event.key == SDLK_RIGHT):
                self.RightButton = False



    def collide(self, aX, aY, bX, bY):
        left_a, top_a, right_a, bottom_a = aX, aY, aX + 80, aY + 96
        left_b, top_b, right_b, bottom_b = bX + 20, bY + 20, bX + 58, bY + 30

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a > bottom_b: return False
        if bottom_a < top_b: return False
        return True



    def map_draw(self, number):
        self.background[number].draw(self.backgroundX, self.backgroundY)
        self.menu_bar.draw(self.menu_barX, self.menu_barY)

        self.scene_bar.draw(self.scene_barX, self.scene_barY)

        self.scene_name[number].draw(self.scene_nameX, self.scene_nameY)
        self.qa[number].draw(self.qaX, self.qaY)



        if (self.switch_state[0] == False):
            self.switch_on.draw(self.switch_X[0], self.switch_Y[0])
        else:
            self.switch_off.draw(self.switch_X[0], self.switch_Y[0] + 30)

        if (self.switch_state[1] == False):
            self.switch_on.draw(self.switch_X[1], self.switch_Y[1])
        else:
            self.switch_off.draw(self.switch_X[1], self.switch_Y[1] + 30)

        if (self.switch_state[2] == False):
            self.switch_on.draw(self.switch_X[2], self.switch_Y[2])
        else:
            self.switch_off.draw(self.switch_X[2], self.switch_Y[2] + 30)

        if(self.Scene_number < 9):
            self.background[number + 1].draw(self.backgroundX + 1024, self.backgroundY)
            self.menu_bar.draw(self.menu_barX + 1024, self.menu_barY)

            self.scene_bar.draw(self.scene_barX + 1024, self.scene_barY)

            self.scene_name[number + 1].draw(self.scene_nameX + 1024, self.scene_nameY)
            self.qa[number + 1].draw(self.qaX + 1024, self.qaY)

            self.switch_on.draw(self.switch_X[0] + 1024, self.switch_Y[0])

            self.switch_on.draw(self.switch_X[1] + 1024, self.switch_Y[1])

            self.switch_on.draw(self.switch_X[2] + 1024, self.switch_Y[2])

        self.hero.draw(self.HeroX, self.HeroY)
        pass



    def map_move(self):
        self.backgroundX -= 5.6
        self.menu_barX -= 5.6
        self.scene_barX -= 5.6
        self.scene_nameX -= 5.6
        self.qaX -= 5.6
        for i in range(0, 3):
            self.switch_X[i] -= 5.6


    def hero_move(self):

        if(self.isCorrect == 0):
            if (self.LeftButton and self.HeroX > 0):
                self.HeroX -= 4
            if (self.RightButton and self.HeroX < 946):
                self.HeroX += 4

        self.HeroY -= 10

        if (self.HeroY < 462):
            self.HeroY += (self.DropSpeed / 10 * 2)
            self.DropSpeed += 1
        else:
            self.DropSpeed = 10
            if(self.isCorrect != 2):
                self.jump_sound.play()

        pass


    def hero_switch(self):

        if(self.collide(self.HeroX, self.HeroY, 300, 518) and self.clearView == False):
            self.switch_state[0] = True
            self.clearView = True

            if(self.correct_list[self.Scene_number] == 1):
                self.answer = 1
                self.isCorrect = 1
                self.clear_sound.play()


            else:
                self.isCorrect = 2
                self.reset_sound.play()

            self.clearTimer = SDL_GetTicks()
            self.switch_sound.play()


        if(self.collide(self.HeroX, self.HeroY, 550, 518) and self.clearView == False):
            self.switch_state[1] = True
            self.clearView = True

            if (self.correct_list[self.Scene_number] == 2):
                self.answer = 2
                self.isCorrect = 1
                self.clear_sound.play()

            else:
                self.isCorrect = 2
                self.reset_sound.play()

            self.clearTimer = SDL_GetTicks()
            self.switch_sound.play()

        if(self.collide(self.HeroX, self.HeroY, 800, 518) and self.clearView == False):
            self.switch_state[2] = True
            self.clearView = True

            if (self.correct_list[self.Scene_number] == 3):
                self.answer = 3
                self.isCorrect = 1
                self.clear_sound.play()

            else:
                self.isCorrect = 2
                self.reset_sound.play()

            self.clearTimer = SDL_GetTicks()
            self.switch_sound.play()


        pass



    def scene_change(self):

        for i in range(0, 3):
            self.switch_state[i] = False
        self.clearView = False
        self.isCorrect = 0
        self.answer = 0
        self.clearTimer = 0

        if(self.Scene_number == 10):
            self.main_sound.stop()
            self.end_sound.play()
        pass


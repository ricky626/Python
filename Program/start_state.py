import pygame
from pygame.locals import *
import time # time 모듈을 import

pygame.init() # pygame 라이브러리 초기화

from data import *

WINDOW_SIZE = (1024, 768) # 윈도우 해상도를 800 X 600으로 초기화
SCREEN = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption('프로그램') # 타이틀 바의 텍스트를 조정


TARGET_FPS = 60 # 초당 프레임을 60으로 설정
clock = pygame.time.Clock() # 60 FPS를 맞추기 위한 딜레이를 추가

running = True # 메인 루프 상태 변수



data = Data()


def update():

    pass
   # print(pygame.time.Clock.get_fps())

def handle_events():
    global running


    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        data.handle_events(event)

def draw():
    SCREEN.fill(WHITE) # 화면을 하얀색으로 채우기


    data.draw(SCREEN)



    pygame.display.update() # 화면 업데이트


while running: # 메인 루프

    handle_events()  # 키보드, 마우스등 각종 이벤트가 발생하는 곳
    update()  # 프로그램의 정보를 지속적으로 업데이트 해주는 부분
    draw()  # 이미지나 도형 등 화면에 무언가 출력을 하는 부분

    clock.tick(TARGET_FPS)  # 프레임 수 맞추기
    #print(clock.get_fps())

pygame.quit() # 프로그램 종료
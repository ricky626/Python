import pygame # pygame 모듈을 import
import time # time 모듈을 import
from pygame.locals import *
pygame.init() # pygame 라이브러리 초기화

WINDOW_SIZE = (800, 600) # 윈도우 해상도를 800 X 600으로 초기화
WHITE = (255, 255, 255) # 하얀색 정의
BLUE = (0, 0, 255) # 파란색 정의

SCREEN = pygame.display.set_mode(WINDOW_SIZE) # 윈도우 해상도 설정
pygame.display.set_caption('My Program') # 타이틀 바의 텍스트를 조정

running = True # 메인 루프 상태 변수

# 메인 루프 안에서 FPS(초당 프레임 수)를 맞추기 위한 딜레이를 추가해주는 코드
TARGET_FPS = 60 # 초당 프레임을 60으로 설정
clock = pygame.time.Clock() # 60 FPS를 맞추기 위한 딜레이를 추가

fontObj = pygame.font.Font("myFont.ttf", 32) # 현재 디렉토리로부터 폰트로딩, 텍스트 크기
state = "안녕하세요" # 마우스 이벤트 상태를 나타내는

def update():
    global running
    clock.tick(TARGET_FPS)  # 프레임 수 맞추기

def handle_events():
    global running
    MOUSE_LEFT = 1  # 마우스 왼쪽 버튼에 대한 버튼 인덱스
    MOUSE_WHEEL_CLICK = 2  # 마우스 휠 클릭에 대한 버튼 인덱스
    MOUSE_RIGHT = 3  # 마우스 오른쪽 버튼에 대한 버튼 인덱스
    MOUSE_WHEEL_UP = 4  # 마우스 휠을 위로 올렸을 때에 대한 버튼 인덱스
    MOUSE_WHEEL_DOWN = 5  # 마우스 휠을 아래로 내렸을 때에 대한 버튼 인덱스

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN: # 마우스 버튼을 눌렀을 때
            if event.button == MOUSE_LEFT: # 마우스 왼쪽 버튼을 눌렀을 때
                state = ("마우스 왼쪽 클릭")
            elif event.button == MOUSE_RIGHT: # 마우스 오른쪽 버튼을 눌렀을 때
                state = ("마우스 오른쪽 클릭")
            elif event.button == MOUSE_WHEEL_CLICK: # 마우스 휠 버튼을 눌렀을 때
                state = ("마우스 휠을 클릭")
            elif event.button == MOUSE_WHEEL_UP: # 마우스 휠을 올렸을 때
                state = ("마우스 휠을 올림")
            elif event.button == MOUSE_WHEEL_DOWN: # 마우스 휠을 내렸을 때
                state = ("마우스 휠을 내림")


def draw():
    SCREEN.fill(WHITE) # 화면을 하얀색으로 채우기
 # 텍스트 객체를 생성! 파리미터 : 텍스트 내용, 안티 앨리어싱 사용 여부, 텍스트 컬러
    textSurfaceObj = fontObj.render(state, True, BLUE) # 텍스트 객체를 생성
    textRectObj = textSurfaceObj.get_rect() # 텍스트 객체의 출력 위치를 가져온다.
    textRectObj.center = (350, 300)  # 텍스트 객체의 중심 좌표를 350, 300으로 설정
    SCREEN.blit(textSurfaceObj, textRectObj) # 설정한 위치에 텍스트 객체를 출력

    pygame.display.update() # 화면 업데이트


while running: # 메인 루프
    handle_events()  # 키보드, 마우스등 각종 이벤트가 발생하는 곳
    update()  # 프로그램의 정보를 지속적으로 업데이트 해주는 부분
    draw()  # 이미지나 도형 등 화면에 무언가 출력을 하는 부분

pygame.quit() # 프로그램 종료

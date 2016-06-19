import urllib.request
import xml.etree.ElementTree as etree

import pygame
from pygame.locals import *
from my_data import GetData


#### DEFINE ####

WHITE = (255, 255, 255) # 하얀색 정의
BLUE = (0, 0, 255) # 파란색 정의
BLACK = (0, 0, 0)
MOUSE_LEFT = 1  # 마우스 왼쪽 버튼에 대한 버튼 인덱스
MOUSE_WHEEL_CLICK = 2  # 마우스 휠 클릭에 대한 버튼 인덱스
MOUSE_RIGHT = 3  # 마우스 오른쪽 버튼에 대한 버튼 인덱스
MOUSE_WHEEL_UP = 4  # 마우스 휠을 위로 올렸을 때에 대한 버튼 인덱스
MOUSE_WHEEL_DOWN = 5  # 마우스 휠을 아래로 내렸을 때에 대한 버튼 인덱스

#### DEFINE ####


my_data = GetData()

class Data:


    def __init__(self):
        ### 데이터 로드 ###
        self.codename_list = my_data.fileread("res/data/지점번호.txt")
        self.name_list = my_data.fileread("res/data/지점명.txt") # 대관령
        self.month_list = my_data.fileread("res/data/월별.txt") # 대관령
        self.angle_list = my_data.fileread("res/data/각도별.txt") # 대관령

        self.name_select = False # 메뉴 name 이 선택되었나요? 판단하는 변수
        self.month_select = False # 메뉴 month 이 선택되었나요? 판단하는 변수
        self.angle_select = False # 메뉴 angle 이 선택되었나요? 판단하는 변수

        self.name_page = 0 # 마우스로 메뉴를 스크롤 하기 위한 변수 마우스 휠로 몇번 내렸는지를 세어준다.
        self.month_page = 0 # 마우스로 메뉴를 스크롤 하기 위한 변수 마우스 휠로 몇번 내렸는지를 세어준다.
        #self.angle_page = 0 # 마우스로 메뉴를 스크롤 하기 위한 변수 마우스 휠로 몇번 내렸는지를 세어준다.

        self.name_KeyCheck = -100 # 마우스로 선택된 이름을 기억해주는 변수
        self.month_KeyCheck = -100 # 마우스로 선택된 달을 기억해주는 변수
        self.angle_KeyCheck = -100 # 마우스로 선택된 각도를 기억해주는 변수




        self.name100_list = my_data.fileread("res/data/대관령.txt") # 대관령
        self.name101_list = my_data.fileread("res/data/춘천.txt") # 춘천
        self.name105_list = my_data.fileread("res/data/강릉.txt") # 강릉
        self.name108_list = my_data.fileread("res/data/서울.txt") # 서울
        self.name112_list = my_data.fileread("res/data/인천.txt") # 인천
        self.name114_list = my_data.fileread("res/data/원주.txt") # 원주
        self.name119_list = my_data.fileread("res/data/수원.txt") # 수원
        self.name129_list = my_data.fileread("res/data/서산.txt") # 서산
        self.name131_list = my_data.fileread("res/data/청주.txt") # 청주
        self.name133_list = my_data.fileread("res/data/대전.txt") # 대전
        self.name135_list = my_data.fileread("res/data/추풍령.txt") # 추풍령
        self.name136_list = my_data.fileread("res/data/안동.txt") # 안동
        self.name138_list = my_data.fileread("res/data/포항.txt") # 포항
        self.name143_list = my_data.fileread("res/data/대구.txt") # 대구
        self.name146_list = my_data.fileread("res/data/전주.txt") # 전주
        self.name156_list = my_data.fileread("res/data/광주.txt") # 광주
        self.name159_list = my_data.fileread("res/data/부산.txt") # 부산
        self.name165_list = my_data.fileread("res/data/목포.txt") # 목포
        self.name169_list = my_data.fileread("res/data/흑산도.txt") # 흑산도
        self.name184_list = my_data.fileread("res/data/제주.txt") # 제주
        self.name185_list = my_data.fileread("res/data/고산.txt") # 고산
        self.name192_list = my_data.fileread("res/data/진주.txt") # 진주

        ### 폰트 로드 ###
        self.font20 = pygame.font.Font("res/font/malgun.ttf", 20)
        self.font30b = pygame.font.Font("res/font/malgunbd.ttf", 30)
        self.font30 = pygame.font.Font("res/font/malgun.ttf", 30)
        self.font50 = pygame.font.Font("res/font/malgun.ttf", 50)
        #self.font80 = pygame.font.Font("res/font/malgun.ttf", 80)

        pass




    def collide(self, aX, aY, bX, bY, bsizeX, bsizeY): # 마우스 + 버튼 간 충돌처리하는 부분
        left_a, top_a, right_a, bottom_a = aX, aY, aX, aY
        left_b, top_b, right_b, bottom_b = bX, bY, bX + bsizeX, bY + bsizeY

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a > bottom_b: return False
        if bottom_a < top_b: return False
        return True



    def update(self):

        pass



    def draw(self, SCREEN): # 그리는 부분

        ### 아래 배경 회색을 출력 ###
        pygame.draw.polygon(SCREEN, (150, 150, 150), ((0, 450), (1024, 450), (1024, 768), (0, 768)))

        ### 지점명 출력 ###
        pygame.draw.polygon(SCREEN, (200, 200, 200), ((190, 550), (290, 550), (290, 700), (190, 700)))
        SCREEN.blit(self.font30b.render("지점명", True, BLACK), (195, 500))
        for i in range(self.name_page, self.name_page + 5):
            SCREEN.blit(self.font20.render(self.name_list[i], True, BLACK), (200, 550 + (i * 30) - (self.name_page * 30))) # 지점명 출력


        ### 월별 출력 ###
        pygame.draw.polygon(SCREEN, (200, 200, 200), ((390, 550), (490, 550), (490, 700), (390, 700)))
        SCREEN.blit(self.font30b.render("날짜별", True, BLACK), (395, 500))
        for i in range(self.month_page, self.month_page + 5):
            SCREEN.blit(self.font20.render(self.month_list[i], True, BLACK), (400, 550 + (i * 30) - (self.month_page * 30))) # 1월 ~ 12월 출력

        ### 각도 출력 ###
        pygame.draw.polygon(SCREEN, (200, 200, 200), ((590, 550), (690, 550), (690, 700), (590, 700)))
        SCREEN.blit(self.font30b.render("각도별", True, BLACK), (595, 500))
        for i in range(0, 4):
            SCREEN.blit(self.font20.render(self.angle_list[i], True, BLACK), (600, 550 + (i * 30))) # 각도 출력


        ### 검색버튼 출력 ###
        pygame.draw.polygon(SCREEN, (255, 100, 200), ((775, 550), (875, 550), (875, 650), (775, 650))) # 775, 350, 875, 450
        SCREEN.blit(self.font50.render("검색", True, BLACK), (774, 560))
        ### 검색버튼 출력 ###

        ### 지점명이 선택되었을 때 박스 출력 ###
        if(self.name_select == True):
            if(self.name_KeyCheck >= self.name_page and self.name_KeyCheck - self.name_page < 5):
                pygame.draw.line(SCREEN, BLACK, [190, 550 + (self.name_KeyCheck * 30) - (self.name_page * 30)], [290, 550 + (self.name_KeyCheck * 30) - (self.name_page * 30)], 5)
                pygame.draw.line(SCREEN, BLACK, [290, 550 + (self.name_KeyCheck * 30) - (self.name_page * 30)], [290, 580 + (self.name_KeyCheck * 30) - (self.name_page * 30)], 5)
                pygame.draw.line(SCREEN, BLACK, [290, 580 + (self.name_KeyCheck * 30) - (self.name_page * 30)], [190, 580 + (self.name_KeyCheck * 30) - (self.name_page * 30)], 5)
                pygame.draw.line(SCREEN, BLACK, [190, 580 + (self.name_KeyCheck * 30) - (self.name_page * 30)], [190, 550 + (self.name_KeyCheck * 30) - (self.name_page * 30)], 5)

        ### 월별이 선택되었을 때 박스 출력 ###
        if(self.month_select == True):
            if(self.month_KeyCheck >= self.month_page and self.month_KeyCheck - self.month_page < 5):
                pygame.draw.line(SCREEN, BLACK, [390, 550 + (self.month_KeyCheck * 30) - (self.month_page * 30)], [490, 550 + (self.month_KeyCheck * 30) - (self.month_page * 30)], 5)
                pygame.draw.line(SCREEN, BLACK, [490, 550 + (self.month_KeyCheck * 30) - (self.month_page * 30)], [490, 580 + (self.month_KeyCheck * 30) - (self.month_page * 30)], 5)
                pygame.draw.line(SCREEN, BLACK, [490, 580 + (self.month_KeyCheck * 30) - (self.month_page * 30)], [390, 580 + (self.month_KeyCheck * 30) - (self.month_page * 30)], 5)
                pygame.draw.line(SCREEN, BLACK, [390, 580 + (self.month_KeyCheck * 30) - (self.month_page * 30)], [390, 550 + (self.month_KeyCheck * 30) - (self.month_page * 30)], 5)

        ### 각도가 선택되었을 때 박스 출력 ###
        if(self.angle_select == True):
            pygame.draw.line(SCREEN, BLACK, [590, 550 + (self.angle_KeyCheck * 30)], [690, 550 + (self.angle_KeyCheck * 30)], 5)
            pygame.draw.line(SCREEN, BLACK, [690, 550 + (self.angle_KeyCheck * 30)], [690, 580 + (self.angle_KeyCheck * 30)], 5)
            pygame.draw.line(SCREEN, BLACK, [690, 580 + (self.angle_KeyCheck * 30)], [590, 580 + (self.angle_KeyCheck * 30)], 5)
            pygame.draw.line(SCREEN, BLACK, [590, 580 + (self.angle_KeyCheck * 30)], [590, 550 + (self.angle_KeyCheck * 30)], 5)


        ### 프로그램 제목 출력 ###
        SCREEN.blit(self.font50.render("20년 평균 일조량", True, BLACK), (300, 10))


        ### 결과창 출력 ###
        if(self.name_KeyCheck != -100):
            SCREEN.blit(self.font50.render(self.name_list[self.name_KeyCheck], True, BLUE), (230, 150))
        if(self.month_KeyCheck != -100):
            SCREEN.blit(self.font50.render(self.month_list[self.month_KeyCheck], True, BLUE), (430, 150))
        if(self.angle_KeyCheck != -100):
            SCREEN.blit(self.font50.render(self.angle_list[self.angle_KeyCheck], True, BLUE), (630, 150))
        pass


    def handle_events(self, event): # 키보드, 마우스 입력 처리

        if(event.type == pygame.MOUSEBUTTONDOWN):
            (mx, my) = pygame.mouse.get_pos() # 마우스가 클릭된 좌표를 얻어온다.

            if(event.button == MOUSE_LEFT):

                ### 마우스로 지점명을 클릭하면 ###
                for i in range(self.name_page, self.name_page + 5):
                    if(self.collide(mx, my, 190, 550 + (i * 30) - (self.name_page * 30), 100, 30)):
                        self.name_KeyCheck = i # 어떤 것이 선택되었는지 알려준다.
                        
                        self.name_select = True # 지점명이 선택되었다. False -> True
                        if(self.month_select):
                            self.month_select = False
                        if(self.angle_select):
                            self.angle_select = False
                            
                ### 마우스로 1월~12월을 클릭하면 ###
                for i in range(self.month_page, self.month_page + 5):
                    if(self.collide(mx, my, 390, 550 + (i * 30) - (self.month_page * 30), 100, 30)):
                        self.month_KeyCheck = i # 어떤 것이 선택되었는지 알려준다.
                        
                        self.month_select = True # 1월~12월이 선택되었다.
                        if(self.name_select):
                            self.name_select = False
                        if(self.angle_select):
                            self.angle_select = False

                ### 마우스로 각도를 클릭하면 ###
                for i in range(0, 4):
                    if(self.collide(mx, my, 590, 550 + (i * 30), 100, 30)):
                        self.angle_KeyCheck = i # 어떤 것이 선택되었는지 알려준다.
                        
                        self.angle_select = True # 각도가 선택되었다.
                        if(self.name_select):
                            self.name_select = False
                        if(self.month_select):
                            self.month_select= False

                #
                # ### 마우스의 좌표와 지점명이 충돌했다면 ###
                # if(self.collide(mx, my, 190, 500, 100, 30)):
                #     self.name_select = True
                #
                # ### 마우스의 좌표와 월별이 충돌했다면 ###
                # if(self.collide(mx, my, 390, 500, 100, 30)):
                #     self.month_select = True
                #
                # ### 마우스의 좌표와 각도가 충돌했다면 ###
                # if(self.collide(mx, my, 590, 500, 100, 30)):
                #     self.angle_select = True

                pass
            
            ### 이름이 선택되면 ###
            if(self.name_select == True):
                if(event.button == MOUSE_WHEEL_DOWN):
                    if(self.name_page < 22 - 5):
                        self.name_page += 1

                if(event.button == MOUSE_WHEEL_UP):
                    if(self.name_page > 0):
                        self.name_page -= 1
                        
            ### 1월~12월이 선택되면 ###            
            if(self.month_select == True):
                if(event.button == MOUSE_WHEEL_DOWN):
                    if(self.month_page < 12 - 5):
                        self.month_page += 1

                if(event.button == MOUSE_WHEEL_UP):
                    if(self.month_page > 0):
                        self.month_page -= 1


                pass


        pass




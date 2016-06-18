

class GetData:


    def __init__(self):

        # self.codename_list = self.fileread("res/data/지점번호.txt")
        # self.name_list = self.fileread("res/data/지점명.txt") # 대관령
        # self.month_list = self.fileread("res/data/월별.txt") # 대관령
        # self.angle_list = self.fileread("res/data/각도별.txt") # 대관령
        #
        #
        # self.name100_list = self.fileread("res/data/대관령.txt") # 대관령
        # self.name101_list = self.fileread("res/data/춘천.txt") # 춘천
        # self.name105_list = self.fileread("res/data/강릉.txt") # 강릉
        # self.name108_list = self.fileread("res/data/서울.txt") # 서울
        # self.name112_list = self.fileread("res/data/인천.txt") # 인천
        # self.name114_list = self.fileread("res/data/원주.txt") # 원주
        # self.name119_list = self.fileread("res/data/수원.txt") # 수원
        # self.name129_list = self.fileread("res/data/서산.txt") # 서산
        # self.name131_list = self.fileread("res/data/청주.txt") # 청주
        # self.name133_list = self.fileread("res/data/대전.txt") # 대전
        # self.name135_list = self.fileread("res/data/추풍령.txt") # 추풍령
        # self.name136_list = self.fileread("res/data/안동.txt") # 안동
        # self.name138_list = self.fileread("res/data/포항.txt") # 포항
        # self.name143_list = self.fileread("res/data/대구.txt") # 대구
        # self.name146_list = self.fileread("res/data/전주.txt") # 전주
        # self.name156_list = self.fileread("res/data/광주.txt") # 광주
        # self.name159_list = self.fileread("res/data/부산.txt") # 부산
        # self.name165_list = self.fileread("res/data/목포.txt") # 목포
        # self.name169_list = self.fileread("res/data/흑산도.txt") # 흑산도
        # self.name184_list = self.fileread("res/data/제주.txt") # 제주
        # self.name185_list = self.fileread("res/data/고산.txt") # 고산
        # self.name192_list = self.fileread("res/data/진주.txt") # 진주


        pass


    def fileread(self, filename):
        f = open(filename, 'r')
        return f.read().split()



 
    def test_print(self):



        pass


g_data = GetData()



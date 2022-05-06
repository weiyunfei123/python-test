# 作者：Wei
# 时间 2022/4/3 20:20

import math

class ZH1:

    def __init__(self):
        print("这是空间直角坐标转换成大地坐标")
        self.X,self.Y,self.Z=eval(input("请输入空间直角坐标,X(以米为单位)，Y(以米为单位)，Z(以米为单位)，格式：X,Y,Z："))

    def selectReference(self):
        global a, b, s
        reference = eval(input("请选择需要依据的椭球，1表示克拉索夫斯基椭球,2表示1975国际椭球，3表示WGS84椭球，4表示CGCS2000椭球:"))
        if reference == 1:
            s = "克拉索夫斯基椭球"
            a = 6378245.0000000000
            b = 6356863.0187730473
        elif reference == 2:
            s = "1975国际椭球"
            a = 6378140.0000000000
            b = 6356755.2881575287
        elif reference == 3:
            s = "WGS84椭球"
            a = 6378137.0000000000
            b = 6356752.3142451795
        elif reference == 4:
            s = "CGCS2000椭球"
            a = 6378137.0000000000
            b = 6356752.3141403558

    def kongjian2dadi(self):
        global B, L, H
        e = math.sqrt((a * a - b * b) / (a * a))

        L = math.atan2(self.Y, self.X)
        L = L * 180 / math.pi  # 弧度转角度

        tanB1 = self.Z / (math.sqrt(self.X * self.X + self.Y * self.Y))
        tanB2 = (self.Z + (a * e * e * tanB1) / math.sqrt(1 + (1 - e * e) * tanB1 * tanB1)) / (math.sqrt(self.X * self.X + self.Y * self.Y))
        while (abs(tanB2 - tanB1) >= 0.00000000001):
            tanB1 = tanB2
            tanB2 = (self.Z + (a * e * e * tanB1) / math.sqrt(1 + (1 - e * e) * tanB1 * tanB1)) / (math.sqrt(self.X * self.X + self.Y * self.Y))
        B = math.atan(tanB2)

        N = a / ((1 - e * e * math.sin(B) * math.sin(B))) ** (1 / 2)

        H = math.sqrt(self.X * self.X + self.Y * self.Y) / math.cos(B) - N

        B = B * 180 / math.pi  # 弧度转角度

    def showResults(self):
            print("根据{},空间直角坐标转换成大地坐标结果为：大地纬度B={:.3f}，大地经度L={:.3f}，大地高H={:.3f}".format(s, B, L, H))

class ZH2(ZH1):
    def __init__(self):
        print("这是大地坐标转空间直角坐标")
        B, L, H = eval(input("请输入大地坐标,B为大地纬度(以°为单位)，L为大地经度(以°为单位)，H为大地高(以米为单位)，格式：B，L，H："))
        self.B= (B * math.pi) / 180
        self.L=(L * math.pi) / 180  # 角度转弧度
        self.H=H
    def dadi2kongjian(self):
        global X, Y, Z
        e = math.sqrt((a * a - b * b) / (a * a))
        N = a / (math.sqrt(1 - e * e * math.sin(self.B) * math.sin(self.B)))

        X = (N + self.H) * math.cos(self.B) * math.cos(self.L)
        Y = (N + self.H) * math.cos(self.B) * math.sin(self.L)
        Z = (N * (1 - e * e) + self.H) * math.sin(self.B)

    def showResults(self):
        print("根据{},大地坐标系转换成空间直角坐标系结果为：X={:.3f}，Y={:.3f}，Z={:.3f}".format(s, X, Y, Z))


def showInterface():
    print('''
               * * * * * 欢迎来到坐标转换小程序* * * * * *
              空间直角坐标转换成大地坐标 or 大地坐标转空间直角坐标
            * * * * * * * * * * * * * * * * * * * * * * * 

            ''')
showInterface()

kj2dd=ZH1()
kj2dd.selectReference()
kj2dd.kongjian2dadi()
kj2dd.showResults()

print('  * * * * * * * * * * * * * * * * * * * * * * * ')

dd2kj=ZH2()
dd2kj.selectReference()
dd2kj.dadi2kongjian()
dd2kj.showResults()


#-2640504.2456,3989366.7432,4204252.104
#41.5,123.5,120.5
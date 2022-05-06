# 作者：Wei
# 时间 2022/4/3 20:20

import math

def showInterface():
    print('''
       * * * * * 欢迎来到坐标转换小程序* * * * * *
      空间直角坐标转换成大地坐标 or 大地坐标转空间直角坐标
    * * * * * * * * * * * * * * * * * * * * * * * 

    ''')

def selectReference():
    global a,b,s
    reference=eval(input("请选择需要依据的椭球，1表示克拉索夫斯基椭球,2表示1975国际椭球，3表示WGS84椭球，4表示CGCS2000椭球:"))
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
    else:
        print("您选择的椭球有误,请重新输入：")
        selectReference()

def selectFunction():
    global function
    function = eval(input("请选择您要实现的功能：1表示由空间直角坐标转换大地坐标，2表示由大地坐标转换空间坐标："))
    if function == 1:
        kongjian2dadi()
    elif function == 2:
        dadi2kongjian()
    else:
        print("您输入有误，请重新输入：")
        selectFunction()

def kongjian2dadi():
    X, Y, Z = eval(input("请输入空间直角坐标,X(以米为单位)，Y(以米为单位)，Z(以米为单位)，格式：X,Y,Z："))
    global B,L,H
    e = math.sqrt((a * a - b * b) / (a * a))

    L = math.atan2(Y, X)
    L = L * 180 / math.pi  # 弧度转角度

    tanB1 = Z / (math.sqrt(X * X + Y * Y))
    tanB2 = (Z + (a * e * e * tanB1) / math.sqrt(1 + (1 - e * e) * tanB1 * tanB1)) / (math.sqrt(X * X + Y * Y))
    while (abs(tanB2 - tanB1) >= 0.00000000001):
        tanB1 = tanB2
        tanB2 = (Z + (a * e * e * tanB1) / math.sqrt(1 + (1 - e * e) * tanB1 * tanB1)) / (math.sqrt(X * X + Y * Y))
    B = math.atan(tanB2)

    N = a / ((1 - e * e * math.sin(B) * math.sin(B))) ** (1 / 2)

    H = math.sqrt(X * X + Y * Y) / math.cos(B) - N

    B = B * 180 / math.pi  # 弧度转角度

def dadi2kongjian():
    global X,Y,Z
    B, L, H = eval(input("请输入大地坐标,B为大地纬度(以°为单位)，L为大地经度(以°为单位)，H为大地高(以米为单位)，格式：B，L，H："))
    B = (B * math.pi) / 180  # 角度转弧度
    L = (L * math.pi) / 180  # 角度转弧度
    e = math.sqrt((a * a - b * b) / (a * a))
    print(e)
    N = a / (math.sqrt(1 - e * e * math.sin(B) * math.sin(B)))
    print(N)
    X = (N + H) * math.cos(B) * math.cos(L)
    Y = (N + H) * math.cos(B) * math.sin(L)
    Z = (N * (1 - e * e) + H) * math.sin(B)

def showResults():
    if function==1:
        print("根据{},空间直角坐标转换成大地坐标结果为：大地纬度B={:.10f}，大地经度L={:.10f}，大地高H={:.10f}".format(s, B, L, H))
    elif function==2:
        print("根据{},大地坐标系转换成空间直角坐标系结果为：X={:.3f}，Y={:.3f}，Z={:.3f}".format(s, X, Y, Z))

def main():
    showInterface()
    selectReference()
    selectFunction()
    showResults()

main()

#-2640504.2456,3989366.7432,4204252.104
#41.5,123.5,120.5
# 作者：Wei
# 时间 2022/4/11 16:58
import os
import math

class COORDINATEREAD:
    def __init__(self):
        self.x1=0
        self.x2=0
        self.y1=0
        self.y2=0

    def calculateDistance(self,x1,y1,x2,y2):#计算距离
        s = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return s

    def calculateAngle(self,x1,y1,x2,y2):#计算方位角
        Y = y2 - y1
        X = x2 - x1
        a = math.atan(Y / X)  # 弧度制
        b = a * 180 / math.pi  # 角度值

        if X > 0 and Y > 0:
            b = b
        elif Y > 0 and X == 0:
            b = 90
        elif Y > 0 and X < 0:
            b += 180
        elif Y == 0 and X < 0:
            b = 180
        elif Y < 0 and X < 0:
            b += 180
        elif Y == 0 and X < 0:
            b = 270
        elif Y < 0 and X > 0:
            b += 360
        else:
            b = 0

        du = int(b)#方位角转换成度分秒
        fen = int((b - du) * 60)
        miao = int(((b - du) * 60 - fen) * 60)
        return du,fen,miao

    def save(self,s,du,fen,miao,s1,s2):#存储文件
        results= "{}->{}的距离为：{:.3f}，方位角为{}度{}分{}秒".format(s1, s2, s, du, fen, miao)
        with open(filename2, 'a', encoding="utf-8") as wfile:
            wfile.write(str(results) + "\n")

    def start(self):
        if os.path.exists(filename1):                            #判断文件是否存在
            with open(filename1, "r", encoding="utf-8") as rfile:#打开文件
                #date = rfile.readline()
                #print(type(date))
                while True:#读文件，直到结束
                    date = rfile.readline()
                    #print(type(date))
                    if date=="":break
                    date = date.split()
                    date = list(date)
                    x1 = eval(date[1])
                    y1 = eval(date[2])
                    x2 = eval(date[4])
                    y2 = eval(date[5])
                    s1 = date[0]
                    s2 = date[3]

                    s = self.calculateDistance(x1, y1, x2, y2)  # 计算距离
                    du, fen, miao = self.calculateAngle(x1, y1, x2, y2)  # 计算方位角
                    self.save(s, du, fen, miao, s1, s2)  # 存储文件
        else:
            print("您的磁盘上没有该文件")
            return

c=COORDINATEREAD()
filename1="计算前坐标数据（无逗号）.txt"
filename2="计算后结果2.txt"
c.start()
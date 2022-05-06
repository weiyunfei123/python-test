# 作者：Wei
# 时间 2022/4/11 16:58
import os
import math

filename1="计算前坐标数据（无逗号）.txt"
filename2="计算后结果9.txt"
#def save(lst):
    #with open(filename2, 'a', encoding="utf-8") as wfile:
       # wfile.write(str(lst) + "\n")
    #read()

def read():
    with open(filename1, "r", encoding="utf-8") as rfile:
        line = rfile.readline()
        rfile.seek(0)
        while line:
            date = rfile.readline()
            date = date.split("   ", 5)
            date = list(date)
            x1 = eval(date[1])
            y1 = eval(date[2])
            x2 = eval(date[4])
            y2 = eval(date[5])
            s1 = date[0]
            s2 = date[3]

            s = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            date_list = [s1, x1, x2, s2, x2, y2]
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

            du = int(b)
            fen = int((b - du) * 60)
            miao = int(((b - du) * 60 - fen) * 60)

            lst="{}->{}的距离为：{:.3f}，方位角为{}度{}分{}秒".format(s1, s2, s, du, fen, miao)
            with open(filename2, 'a', encoding="utf-8") as wfile:
                wfile.write(str(lst) + "\n")

def main():
    read()

main()
    #def calculateDistance(self):
        #s = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        #with open(filename2, "w", encoding="utf-8") as wfile:
            #for item in lst:
                #wfile.write(str(lst)+"\n")



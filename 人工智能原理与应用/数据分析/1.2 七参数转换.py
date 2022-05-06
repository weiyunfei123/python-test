# 作者：Wei
# 时间 2022/4/16 12:30

import os
import numpy as np
from math import sin,cos,sqrt,pi

#这是一个84转54坐标
#适合5个公共点

filename1="七参数公共点数据.txt"
filename2="七参数转换后数据.txt"

#创建七参数转化的类
class SevenParameticSwitch:
    # 初始化实例属性
    def __init__(self):
        pass

    # 开始拟转换数据的转换
    def startSwitch(self,Tx,Ty,Tz,Wx,Wy,Wz,m):
        if os.path.exists(filename1):#判断拟转换的数据是否存在
            with open(filename1,"r",encoding="utf-8") as rfile:#打开文件
                date=rfile.readline()#读第一行，第一行不是数据
                while True:
                    date=rfile.readline()#读第二行数据
                    date = date.split()
                    try:
                        s=date[0] # 将点数据名称赋给s
                    except:#退出循环
                        break
                    xa= eval(date[1])# 将拟转换数据横坐标赋给xa
                    ya= eval(date[2])# 将拟转换数据横坐标赋给ya
                    za= eval(date[3])# 将拟转换数据横坐标赋给za
                    R1=np.mat([[1,0,0],[0,cos(Wx),sin(Wx)],[0,-sin(Wx),cos(Wx)]]) #计算旋转矩阵R1
                    R2=np.mat([[cos(Wy),0,-sin(Wy)],[0,1,0],[sin(Wy),0,cos(Wy)]]) #计算旋转矩阵R2
                    R3=np.mat([[cos(Wz),sin(Wz),0],[-sin(Wz),cos(Wz),0],[0,0,1]]) #计算旋转矩阵R3
                    D=np.mat([[Tx],[Ty],[Tz]])+(1+m)*R1*R2*R3*np.mat([[xa],[ya],[za]])#计算最后结果，以矩阵方式
                    x=D[0,0]#取出D中第1行第1列
                    y=D[1,0]#取出D中第2行第1列
                    z=D[2,0]#取出D中第3行第1列

                    self.saveDate(s, x, y,z) # 调用保存数据的函数
        else:
            print("您的磁盘上没有七参数拟转换数据.txt文件！") #磁盘没有拟转换数据的提示

    def saveDate(self,s,x,y,z):
        results="{}  {:.4f}  {:.4f}  {:.4f}".format(s,x,y,z)  #定义保存数据的格式
        with open(filename2,"a",encoding="utf-8") as wfile:  #追加数据
            wfile.write(results+"\n") #写入转换后的数据

    def writeTitle(self):
        title = "点名    X_(54)	     Y_(54)     	Z_(54)" #定义文档标题
        with open(filename2, "w", encoding="utf-8") as wfile:  # 写入数据
            wfile.write(title + "\n")


    def main(self):
        if os.path.exists(filename1):#判断文件是否存在
            with open(filename1,"r",encoding="utf-8") as rfile:
                date=rfile.readline()#先读第一行，第一行不是数据
                date=rfile.readline()#读第二行数据
                date=date.split()#分隔
                xa1=eval(date[1])
                ya1=eval(date[2])
                za1=eval(date[3])
                x1=eval(date[4])
                y1=eval(date[5])
                z1=eval(date[6])
                date = rfile.readline()  # 读第三行数据
                date = date.split()#分隔
                xa2 = eval(date[1])
                ya2 = eval(date[2])
                za2 = eval(date[3])
                x2 = eval(date[4])
                y2 = eval(date[5])
                z2 = eval(date[6])
                date = rfile.readline()  # 读第四行数据
                date = date.split()#分隔
                xa3 = eval(date[1])
                ya3 = eval(date[2])
                za3 = eval(date[3])
                x3 = eval(date[4])
                y3 = eval(date[5])
                z3 = eval(date[6])
                date = rfile.readline()  # 读第五行数据
                date = date.split()#分隔
                xa4 = eval(date[1])
                ya4 = eval(date[2])
                za4 = eval(date[3])
                x4 = eval(date[4])
                y4 = eval(date[5])
                z4 = eval(date[6])
                date = rfile.readline()  # 读第六行数据
                date = date.split()#分隔
                xa5 = eval(date[1])
                ya5 = eval(date[2])
                za5 = eval(date[3])
                x5 = eval(date[4])
                y5 = eval(date[5])
                z5 = eval(date[6])
        else:
            print("您的磁盘上没有七参数公共点数据.txt文件！")  #磁盘没有公共点数据文件的提示
            return
        B=np.mat([
            [1, 0, 0, 0, -za1, ya1, xa1],#计算B
            [0, 1, 0, za1, 0, -xa1, ya1],
            [0, 0, 1, -ya1, xa1, 0, za1],
            [1, 0, 0, 0, -za2, ya2, xa2],  #
            [0, 1, 0, za2, 0, -xa2, ya2],
            [0, 0, 1, -ya2, xa2, 0, za2],
            [1, 0, 0, 0, -za3, ya3, xa3],  #
            [0, 1, 0, za3, 0, -xa3, ya3],
            [0, 0, 1, -ya3, xa3, 0, za3],
            [1, 0, 0, 0, -za4, ya4, xa4],  #
            [0, 1, 0, za4, 0, -xa4, ya4],
            [0, 0, 1, -ya4, xa4, 0, za4],
            [1, 0, 0, 0, -za5, ya5, xa5],  #
            [0, 1, 0, za5, 0, -xa5, ya5],
            [0, 0, 1, -ya5, xa5, 0, za5]
        ])
        l=np.mat([                           #计算l
            [x1-xa1],[y1-ya1],[z1-za1],
            [x2 - xa2], [y2 - ya2], [z2 - za2],
            [x3 - xa3], [y3 - ya3], [z3 - za3],
            [x4 - xa4], [y4 - ya4], [z4 - za4],
            [x5 - xa5], [y5 - ya5], [z5 - za5],
        ])
        X = (B.T * B).I * B.T * l #计算X
        V=B*X-l
        Tx=X[0,0]#取出X中第1行第1列
        Ty = X[1, 0]#取出X中第2行第1列
        Tz = X[2, 0]#取出X中第3行第1列
        Wx = X[3, 0]#取出X中第4行第1列
        Wy = X[4, 0]#取出X中第5行第1列
        Wz = X[5, 0]#取出X中第6行第1列
        m = X[6, 0]#取出X中第7行第1列

        a= 3600*Wx * 180 / pi  # 角度值
        b= 3600*Wy * 180 / pi  # 角度值
        c= 3600*Wz * 180 / pi  # 角度值
        print(Tx,Ty,Tz,a,b,c,m,)
        self.writeTitle()
        self.startSwitch(Tx,Ty,Tz,Wx,Wy,Wz,m) #调用对拟转换数据的转换函数
        m=sqrt(V.T*V/8)
        print("中误差m={}".format(m))

if __name__=="__main__":
    # 实例化四参数转换对象：seven
    seven=SevenParameticSwitch()
    seven.main()#运行主函数

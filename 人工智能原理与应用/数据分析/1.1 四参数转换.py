# 作者：Wei
# 时间 2022/4/15 16:15

import numpy as np
import os

filename1="公共点数据.txt"
filename2="拟转换数据.txt"
filename3="转换后数据.txt"

#创建四参数转化的类
class FourParametricSwitch:
    #初始化实例属性
    def __init__(self):
        pass

    # 开始拟转换数据的转换
    def startSwitch(self,a,b,c,d):
        if os.path.exists(filename2):#判断拟转换的数据是否存在
            with open(filename2,"r",encoding="utf-8") as rfile:#打开文件
                while True:
                    date=rfile.readline() #读一行数据
                    #if date=="":break
                    date = date.split()  # 分隔数据
                    try:
                        s = date[0]  # 将点数据名称赋给s
                    except:
                        break
                    xa = eval(date[1])  # 将拟转换数据横坐标赋给xa
                    ya = eval(date[2])  # 将拟转换数据纵坐标赋给ya
                    x = a + xa * c - ya * d  # 获得转换后数据x
                    y = b + ya * c + xa * d  # 获得转换数据y
                    self.saveDate(s, x, y)  # 调用保存数据的函数
        else:
            print("您的磁盘上没有拟转换数据.txt文件！") #磁盘没有拟转换数据的提示
            return

    # 将转换的数据写入文件中
    def saveDate(self,s,x,y):
        results="{}  {:.4f}  {:.4f}".format(s,x,y) #定义保存数据的格式
        with open(filename3,"a",encoding="utf-8") as wfile: #追加数据
            wfile.write(str(results)+"\n") #写入转换后的数据

    # 主函数
    def main(self):
        if os.path.exists(filename1):#判断文件是否存在
            with open(filename1,"r",encoding="utf-8") as rfile:
                date=rfile.readline()#先读第一行，第一行不是数据
                date = rfile.readline()#读第二行数据
                date = date.split() #分隔
                xa1 = eval(date[1])
                ya1 = eval(date[2])
                x1 = eval(date[4])
                y1 = eval(date[5])
                date = rfile.readline()#读第三行数据
                date = date.split()#分隔
                xa2 = eval(date[1])
                ya2 = eval(date[2])
                x2 = eval(date[4])
                y2 = eval(date[5])
                date = rfile.readline()#读第四行数据
                date = date.split()#分隔
                xa3 = eval(date[1])
                ya3 = eval(date[2])
                x3 = eval(date[4])
                y3 = eval(date[5])
                date = rfile.readline()#读第五行数据
                date = date.split()#分隔
                xa4 = eval(date[1])
                ya4 = eval(date[2])
                x4 = eval(date[4])
                y4 = eval(date[5])
        else:
            print("您的磁盘上没有公共点数据.txt文件！")  #磁盘没有公共点数据文件的提示
            return
        B=np.mat([[1, 0, xa1, -ya1],  #计算B
                  [0, 1, ya1, xa1],
                  [1, 0, xa2, -ya2],
                  [0, 1, ya2, xa2],
                  [1, 0, xa3, -ya3],
                  [0, 1, ya3, xa3],
                  [1, 0, xa4, -ya4],
                  [0, 1, ya4, xa4],])
        l=np.mat([[x1],[y1],[x2],[y2],[x3],[y3],[x4],[y4]]) #计算l
        X=(B.T*B).I*B.T*l #计算X
        a=X[0,0] #取出X中第一行第一列
        b=X[1,0] #取出X中第二行第一列
        c=X[2,0] #取出X中第三行第一列
        d=X[3,0] #取出X中第四行第一列
        self.startSwitch(a,b,c,d) #调用对拟转换数据的转换函数

if __name__=="__main__":
    #实例化四参数转换对象：four
    four=FourParametricSwitch()
    four.main()#运行主函数
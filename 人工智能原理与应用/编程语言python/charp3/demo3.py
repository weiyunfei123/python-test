# 作者：Wei
# 时间 2022/3/17 9:36

#输出9*9的* 到99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(j,i,i*j),end=" ")
    print()

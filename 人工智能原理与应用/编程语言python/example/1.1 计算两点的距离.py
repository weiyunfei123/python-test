# 作者：Wei
# 时间 2022/3/15 8:34
#计算两点的距离计算公式

import math
import time

print("计算两点的距离")
XA,YA=eval(input("请输入A点的坐标XA,YA[用逗号隔开]："))
XB,YB=eval(input("请输入B点的坐标XB,YB[用逗号隔开]："))


start=time.perf_counter()
s=math.sqrt((XB-XA)*(XB-XA)+pow(YB-YA,2))
end=time.perf_counter()
t=end-start
print("两点之间的距离s为{:.10f}，消耗时间为{:.10f}".format(s,t))


# 作者：Wei
# 时间 2022/3/14 21:02
# π的计算

import time
import random
import math

DARTS=2**30
hits=0
start=time.perf_counter()
for i in range(1,DARTS+1):
    x,y=random.random(),random.random()
    distance=math.sqrt(x**2+y**2)
    if distance<1:
        hits=hits+1
pi=4*(hits/DARTS)
end=time.perf_counter()
t=end-start
print("pi的值为{:.10f},运行的时间为{:.5f}".format(pi,t))






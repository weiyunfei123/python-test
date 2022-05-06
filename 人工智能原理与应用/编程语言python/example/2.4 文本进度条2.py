# 作者：Wei
# 时间 2022/3/14 19:40

import time
scale=50
print("执行开始".center(scale//2,"-"))
start=time.perf_counter()
for i in range(scale+1):
    a="*"*i
    b="."*(scale-1)
    c=(i/scale)*100
    end=time.perf_counter()
    t=end-start
    print("\r{:3.0f}%[{}->{}]{:.3f}s".format(c,a,b,t),end="")
    time.sleep(1)
print("\n"+"执行结束".center(scale//2,"-"))


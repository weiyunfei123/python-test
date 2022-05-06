# 作者：Wei
# 时间 2022/3/16 17:51

#计算方位角和距离

import math
print("计算两点的距离及方位角")
x1,y1=eval(input("请输入A点的坐标X1,Y1[用逗号隔开]："))
x2,y2=eval(input("请输入B点的坐标X2,Y2[用逗号隔开]："))
s=math.sqrt((x2-x1)**2+(y2-y1)**2)

Y=y2-y1
X=x2-x1


a = math.atan(Y / X)  # 弧度制
b=a * 180 / math.pi  # 角度值

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





du=int(b)
fen=int((b-du)*60)
miao=int(((b-du)*60-fen)*60)

print("两点之间的距离s为{:.2f},方位角为{}度{}分{}秒".format(s,du,fen,miao))

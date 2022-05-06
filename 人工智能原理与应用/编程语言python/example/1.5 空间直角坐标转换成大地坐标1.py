# 作者：Wei
# 时间 2022/3/17 12:03

#由空间直角坐标转换成大地坐标

import math
print("由空间直角坐标转换成大地坐标")
X,Y,Z=eval(input("请输入空间直角坐标,X(以米为单位)，Y(以米为单位)，Z(以米为单位)，格式：X,Y,Z："))
f=eval(input("请选择需要依据的椭球，克拉索夫斯基椭球请输入1,1975国际椭球请输入2，WGS84椭球请输入3，CGCS2000椭球请输入4:"))

if f==1:
    s="克拉索夫斯基椭球"
    a=6378245.0000000000
    b=6356863.0187730473
elif f==2:
    s ="1975国际椭球"
    a =6378140.0000000000
    b =6356755.2881575287
elif f==3:
    s = "WGS84椭球"
    a =6378137.0000000000
    b =6356752.3142451795
elif f==4:
    s="CGCS2000椭球"
    a=6378137.0000000000
    b=6356752.3141403558
else:
    print("您选择的椭球有误")

e = math.sqrt((a*a-b*b)/(a * a))

L=math.atan2(Y,X)
L=L*180/math.pi  # 弧度转角度

tanB1=Z/(math.sqrt(X*X+Y*Y))
tanB2=(Z+(a*e*e*tanB1)/math.sqrt(1+(1-e*e)*tanB1*tanB1))/(math.sqrt(X*X+Y*Y))
while (abs(tanB2-tanB1)>=0.00000000001):
    tanB1=tanB2
    tanB2=(Z+(a*e*e*tanB1)/math.sqrt(1+(1-e*e)*tanB1*tanB1))/(math.sqrt(X*X+Y*Y))
B=math.atan(tanB2)



N = a/((1 - e *e*math.sin(B)* math.sin(B)))**(1/2)

H=math.sqrt(X*X+Y*Y)/math.cos(B)-N

B=B*180/math.pi  # 弧度转角度

print("根据{},空间直角坐标转换成大地坐标结果为：大地纬度B={:.3f}，大地经度L={:.3f}，大地高H={:.3f}".format(s,B,L,H))

print(N)
#X,Y,Z:-2640504.2456,3989366.7432,4204252.104
#N=6387530.980675858
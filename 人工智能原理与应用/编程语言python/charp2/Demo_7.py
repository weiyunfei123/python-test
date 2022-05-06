# 作者：WeiYunfein1=99
n1=99
n2=-66
n3=0

print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))

print("十进制",110)
print("二进制",0b10101111)
print("八进制",0o176)
print("十六进制",0x1EAf)

a=3.1415926
print(a,type(a))
n1=1.1
n2=2.2
print(n1+n2)#小数不确定的情况

n3=0.5e2
n4=1e2
print(n3+n4)

from decimal import Decimal#解决小数不确定的情况
print(Decimal("1.1")+Decimal("2.2"))
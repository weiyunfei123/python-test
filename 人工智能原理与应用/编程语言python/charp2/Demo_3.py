import math


print(123)
print(12.345)
print(1+2j)
print('hello world')
print("hello world")

print(len('hello world'))

str="hello world"
print(str)

print(66+33)
print(1>2)
print(math.sin(30))

#将数据输出到文件中
'''
fp=open("D:/test.txt",'a+')
print("hello world",file=fp)
fp.close()
'''

#print(*objects,sep="",end="\n",file=)

print("hello","world","python")
print("hello",end=" ")
print("world",end=",")
print("python",end="\n")
print("="*4)

help("keywords")

import keyword
print(keyword.kwlist)

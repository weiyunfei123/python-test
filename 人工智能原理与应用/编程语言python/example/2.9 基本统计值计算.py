# 作者：Wei
# 时间 2022/3/18 14:11

#基本统计值计算

from math import sqrt

def getNum():#获得用户输入
    nums=[]
    iNumStr=input("请输入数字(直接输入回车退出)：")
    while iNumStr!="":
        nums.append((eval(iNumStr)))
        iNumStr=input("请输入数字(直接输入回车退出：)")
    return nums
def mean(n):#计算平均值
    s=0
    for i in n:
        s=s+i
    return s/len(n)
def dev(n,m):#计算标准差
    s=0.0
    for i in n:
        s=s+(i-m)**2
    return sqrt(s/(len(n)-1))
'''
def median(n):#计算中位数
    new=sorted(n)
    s=len(n)
    if s%2==1:
        med=new[(s-1)/2]
    else:
        med=(new[(s/2)-1]+new[(s/2)])/2
    return med
'''

def median(n):#计算中位数
    new=sorted(n)
    s=len(n)
    if s%2==1:
        med=new[s//2]
    else:
        med=(new[s//2-1]+new[s//2])/2
    return med
def main():
    n = getNum()  # n为列表
    m = mean(n)
    d = dev(n, m)
    med = median(n)
    print("您输入的数据平均值为：{},标准差为：{:.2},中位数为：{}".format(m,d,med))
main()



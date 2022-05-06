# 作者：WeiYunfei
# 时间 2022/3/14 9:59
#实现摄氏温度和华氏温度的转换
TempStr=input('请输入带有符号的温度值：')
if TempStr[-1] in ['F','f']:
    C=(eval(TempStr[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F=1.8*eval(TempStr[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误！")

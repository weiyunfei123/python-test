# 作者：WeiYunfei
# 时间 2022/3/9 17:49

a,b=100,200
print ("十进制数为%d"%a)
print("右对齐：%8d"%a)
print("左对齐：%-8d"%a)

f=3.1415926123
print("保留6位有效数字%g"%f)
print("保留小数点后6位有效数字%.6f"%f)
print("设定宽度%15f"%f)

s="adcd"
print("原样输出%s"%s)
print ("设置宽度%8s"%s)
print("设置宽度%-8send"%s)

print("十进制整数形式：{:d}".format(1000))
print("指数形式的浮点数:{:e}".format(123.456))

print("{}:计算机{}的cpu占有率为{}%".format("2022-3-15","python","15"))
print("{1}:计算机{0}的cpu占有率为{2}%".format("2022-3-15","python","15"))
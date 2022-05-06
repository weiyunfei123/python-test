# 作者：Wei
# 时间 2022/3/14 20:25
height,weight=eval(input("请输入身高（米）和体重（公斤）[用逗号隔开]："))
BMI=weight/pow(height,2)
print("BMI数值为：{:.2f}".format(BMI))
who,dom="",""

if BMI<18.5:
    who="偏瘦"
elif BMI<25:
    who="正常"
elif BMI<30:
    who="偏胖"
else:
    who="肥胖"

if BMI < 18.5:
    dom = "偏瘦"
elif BMI < 24:
    who = "正常"
elif BMI < 28:
    dom = "偏胖"
else:
    dom = "肥胖"

print("BMI指标为：国际{},国内{}".format(who,dom))
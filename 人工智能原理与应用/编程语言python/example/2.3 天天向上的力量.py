# 作者：WeiYunfei
# 时间 2022/3/14 17:11

def DayUP(df):
    dayup=1.0
    for i in range(365):
        if i%7 in[6,0]:
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+df)
    return dayup
dayfactor=0.01
while (DayUP(dayfactor)<37.78):
    dayfactor+=0.001
print("每天的努力参数为：{:.3f}.".format(dayfactor))



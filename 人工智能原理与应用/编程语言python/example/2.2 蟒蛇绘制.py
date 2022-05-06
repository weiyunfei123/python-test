# 作者：WeiYunfei
# 时间 2022/3/14 10:01

import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(5)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,40)
turtle.fd(40)
turtle.circle(- 16,180)
turtle.fd(40)
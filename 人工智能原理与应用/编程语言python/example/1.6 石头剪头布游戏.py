# 作者：Wei
# 时间 2022/3/19 18:31

import random

def showInterface():
    print('''
       * * * * * 欢迎来到4399游戏平台* * * * * *
                石头    剪头    步
    * * * * * * * * * * * * * * * * * * * * * * * 

    ''')
def choicePlayer():
    global player_name
    global computer_name
    player_name = input("请输入玩家姓名：")
    print("1.貂蝉 2.吕布 3.诸葛亮")
    choice = eval(input("请选择电脑角色："))
    if choice == 1:
        computer_name = "貂蝉"
    elif choice == 2:
        computer_name = "吕布"
    elif choice == 3:
        computer_name = "诸葛亮"
    else:
        computer_name = "匿名"
    print("{}  VS  {}".format(player_name, computer_name))
def startGame():
    print("游戏开始了")
    global player_score
    global computer_score
    player_score = 0 #初始得分
    computer_score = 0
    while True:
        player_first=eval(input("---------- 请出拳：1.石头   2.剪头   3.布  ----------"))
        if player_first==1:
            player_first_name="石头"
        elif player_first==2:
            player_first_name="剪头"
        elif player_first==3:
            player_first_name="布"
        else:
            player_first_name="石头"
            player_first=1

        computer_first=random.randint(1,3)
        if computer_first==1:
            computer_first_name="石头"
        elif computer_first==2:
            computer_first_name="剪头"
        else:
            computer_first_name="布"

        print (player_name   ," 出拳 ",player_first_name)
        print (computer_name ," 出拳 ",computer_first_name)

        if player_first==computer_first:
            print("平局")
        elif (player_first==1 and computer_first==2) or\
             (player_first==2 and computer_first==3) or \
             (player_first==3 and computer_first==1):
            print("玩家："+player_name+"胜")
            player_score+=1
        else:
            print("电脑：" + computer_name + "胜")
            computer_score+=1
        answer=input("再来一局吗？y/n:")
        if answer=="n":
            break
    return player_score and computer_score

def showResult(player_score,computer_score):
    print("_"*10)
    print("战绩显示:")
    print(player_name,player_score)
    print(computer_name,computer_score)
    print("_"*10)
    if player_score==computer_score:
        print("平局")
    elif player_score>computer_score:
        print(player_name+"胜利")
    else:
        print(computer_name,"胜利")
    print("游戏结束，欢迎下次再来！")


showInterface()#显示界面
choicePlayer()#选择玩家
startGame()#开始游戏
showResult(player_score,computer_score)#显示结果

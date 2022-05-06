# 作者：Wei
# 时间 2022/4/12 20:31

class StudentInformation:
    def __init__(self):
        pass
    def menu(self):
        print("==================学生信息管理系统==================")
        print("----------------------功能菜单----------------------")
        print("                  1.录入学生信息")
        print("                  2.查找学生信息")
        print("                  3.删除学生信息")
        print("                  4.修改学生信息")
        print("                  5.排序")
        print("                  6.统计学生总人数")
        print("                  7.显示学生信息")
        print("                  0.退出")
        print("--------------------------------------------------")
    def main(self):
        while True:
            self.menu()
            choice=input("请选择：")
            if choice==0:
                answer=input("您确定要退出吗？y/n")
                if answer=="y" or "Y":
                    print("感谢您的使用！")
                    break
                else:
                    continue
            elif choice==1:
                self.insert()
            elif choice==2:
                self.search()
            elif choice==3:
                self.delete()
            elif choice==4:
                self.modify()
            elif choice==5:
                self.sort()
            elif choice==6:
                self.total()
            elif choice==7:
                self.show()
            #else:
                #print("您的输入有误，请重新输入！")






s=StudentInformation()
s.main()
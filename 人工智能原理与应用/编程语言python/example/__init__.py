# 作者：WeiYunfei
# 时间 2022/3/14 9:58


'''
fname=input("请输入要打开的文件：")
with open(fname,"r",encoding="utf-8") as rfile:
    for i in rfile.readlines():
        print(i)
        rfile.close()
'''

fname=input("请输入要写入的文件：")
file=open(fname,"w+",encoding="utf-8")
ls=["唐诗","宋词"]
file.writelines(ls)
file.seek(0)
for line in file:
    print(line)
file.close

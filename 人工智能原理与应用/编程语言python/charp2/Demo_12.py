# 作者：WeiYunfei
# 时间 2022/3/10 8:39

str1='人生苦短，我用python'
print(str1,type(str1))
str2="'人生苦短，我用python'"
print(str2,type(str2))

str3='''人生苦短，
我用python'''
print(str3,type(str3))

#索引
s="Hello,python!"
print("字符串\""+s+"\"的长度为："+str(len(s)))
print ("第0个元素："+s[0])
print ("第2个元素："+s[2])
print ("第10个元素："+s[10])
print ("最后一个个元素："+s[-1])

#切片
s="学python，大家一起在努力!"
print(s)
print("字符串\""+s+"\"的长度为："+str(len(s)))
print (s[1:10])
print(s[1:10:2])
print(s[:])
print(s[:5])
print(s[4::])

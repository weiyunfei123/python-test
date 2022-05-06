help("keywords")

import keyword
print(keyword.kwlist)


name='玛利亚'
print(name)

print('标识',id(name))
print('类型',type(name))
print('值',name)

name="楚溜冰"
print(name)
print('标识',id(name))
print('类型',type(name))
print('值',name)

a,b=1,2
b,a=a,b #交换
print(a,b)
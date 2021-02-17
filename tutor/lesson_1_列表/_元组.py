'''
不可改变的列表叫做元组，用()表示
'''

# 通过list函数可以将字符串转化为列表
name = 'bob'
print(name)
print(list(name))
# 用tuple可以将字符串或者列表转化为元组
info = 'information'
print(info)
print(tuple(info))
names = ['lily','shali']
print(names)
print(tuple(names))
#把列表中的某个元素转化为元组
print(tuple(names[1]))


num = (1,2,3,3,2,1,3,3,3)
print(num.count(3))
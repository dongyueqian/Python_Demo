print('浅复制')
'''
dict2 其实是 dict1 的引用（别名），所以输出结果都是一致的，
dict3 父对象进行了深拷贝，不会随dict1 修改而修改，子对象是浅拷贝所以随 dict1 的修改而修改
'''
dict1 = {'user': 'runoob', 'num': [1, 2, 3]}

dict2 = dict1  # 浅拷贝: 引用对象
dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用

# 输出结果
print('dict1:',dict1)
print('dict2:',dict2)
print('dict3',dict3)

print('---------修改 data 数据-----------')
dict1['user'] = 'root'
dict1['num'].remove(1)
dict1['num'].insert(3,4)

# 输出结果
print('dict1:',dict1)
print('dict2:',dict2)
print('dict3',dict3)

print("=================分割线=====================")

print('深复制')

from copy import deepcopy
import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a  # 赋值，传对象的引用
# c = copy.copy(a)  # 对象拷贝，浅拷贝
c = a.copy()

# d = copy.deepcopy(a)  # 对象拷贝，深拷贝
d = deepcopy(a)

a.append(5)  # 修改对象a
a[4].append('e')  # 修改对象a中的['a', 'b']数组对象

print('a = ', a)
print('b = ', b)  # b 与 a 一样
print('c = ', c)  # c 是 a 的浅拷贝，深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用，那么c 字典里面的数组会跟随a
print('d = ', d)  # d 是 a 的深拷贝，完全独立，不受a影响
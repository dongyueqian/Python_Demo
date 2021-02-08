'''
将字符串转换成列表
'''
name = 'Lily'
print(name)
print(list(name))

'''
列表元素的增 删 改
'''
print('=======================分割线=======================')
x = [15,'llll','shalu',66,89,100]
print('原始列表：',x)

print('=======================分割线 ： append增  =======================')

x.append(222)   #增加一个元素
print('增加(追加) 222 后的列表：',x)
x.append(['大课间','间谍'])  #['大课间','间谍']是一个元素
print('增加(追加) 一个列表 后的列表：',x)

print('=======================分割线 ： extend增 =======================')

x.extend(['倩','dyq']) #extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表），增加多个元素
print('再增加(追加) 一个列表 后的列表：',x)
x.extend('月倩')
print('增加(追加) 一个字符串 后的列表：',x)

print('=======================分割线 ： insert插入=======================')

x.insert(2,'hahaha')
print('在第2的位置增加  hahaha  后的列表：',x)

print('=======================分割线 ： 删除 =======================')

x.remove(66)
print('删除元素 41 后的列表：',x)

del x[3]
print('删除 索引为3 的元素后的列表',x)

x.pop()
print('弹出末尾的元素后的列表',x)
x.pop(7)
print('弹出 索引为7 的元素后的列表',x)

print('=======================分割线 ： 修改=======================')

x[5] = 'kkkkkk' #修改
print('修改第5个元素为 kkkkkk 后的列表',x)
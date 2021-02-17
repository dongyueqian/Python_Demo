'''
列表的操作：count、reverse
'''
nums = [1,2,3,4,5,6,8,3,4,6,5,2,2,2,2,4]
names = ['lily','bob','tom','xiaoming','lily']
print(nums.count(2))
print(names.count('lily'))

nums.reverse()
print(nums)

names.reverse()
print(names)

print('*******************分割线************************')
'''
sort 、sorted 排序
sort：对自身列表进行排序，因此返回的是None
sorted： 对原列表不进行任何改变
'''
nums2 = [1,12,3,14,5,6,18,3,45,6,5,22,2,42,26,4]
print('原列表nums2：',nums2)
nums2.sort()
print('把nums2排序后的列表：',nums2)

print('*******************分割线************************')

x = [4,6,1,3,7,9,2]
y = x.sort()
print(x)
print(y) # 输出None，因为 x.sort() 是对 x 进行排序，返回的结果是None

print('*******************分割线************************')

# 优化：
y = x #让 y 指向 x，再把 x 排序
x.sort()
print('x:',x)
print('y:',y)

print('*******************分割线************************')

# 或者用sorted
x1 = [3,2,1,15,27,8,9]
y1 = sorted(x1) # 对 x1 进行排序 赋值给 y1 ，x1 不变
print('x1:',x1)
print('y1:',y1)
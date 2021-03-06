'''
分片是取一定范围内的数据，分片的结束点索引针对的元素取不到

开始点（最左）的元素包含在结果中，而结束点（最右边的元素）不包含在结果中

当使用一个负数作为步长时，起始点的索引要大于结束点的索引

没有指定开始点和结束点索引，正数步长会从序列的头部开始向右提取元素；而步长为负数的，则从序列的尾部开始向左提取元素

'''

num  = [0,1,2,3,4,5,6,7,8,9,10]

# 分片
print(num[ 0 : 4 ]) # 0 <= x < 4 : 0,1,2,3
print(num[ 2 : 8 ]) # 2 <= x < 7 : 2,3,4,5,6,7
print(num[ -3 : -1 ]) # -3 <= x < -1 : 8,9
print(num[ -1 : ]) #  10
print(num[ 7 : 10 ]) # 7 <= x <10 : 7,8,9

#步长
print(num[1:8:2])  # 1,3,5,7
print(num[1:9:3])  # 1,4,7
print(num[::2])  # 2,4,6,8,10
print(num[::1])  #原始数组
print(num[::-1]) # 原始数组倒叙输出
print(num[::-2])  # 2步长倒叙输出
print(num[-10:-2:1]) # 1~8
print(num[-10:-2:3]) # 1,4,7

'''
列表无法与字符串进行运算
'''
print('*****************分割线**************')
num1 = [3,4,5]
num2 = [6,7,8]
print(num1+num2)
str1 = '12234234j'
str2 = 'sdhjsjdhe2222'
print(str1 + str2)
# print(num1 + str1) #列表无法与字符串进行运算
print(num1 * 5)
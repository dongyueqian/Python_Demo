'''
列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，
用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。

每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。
返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。
如果希望表达式推导出一个元组，就必须使用括号

'''
vec = [2, 4, 6]
l = []
for i in vec:
    i = i * 3
    l.append(i)
print(l)
print("-----------1-------------")
# 用列表推导式优化
# 将列表中每个数值乘三，获得一个新的列表
a = [i * 3 for i in vec]
print(a)
print("-----------2-------------")
# 再难一点
c = [[i , i ** 2] for i in vec]
print(c)

print("-----------3-------------")

# 对序列里每一个元素逐个调用某方法
numbers = ['  dubdhd ', '  hhh ','  kkk ']
num = [i.strip() for i in numbers ]
print(num)

print("------------4------------")
# 用 if 子句作为过滤器
d = [3*i for i in vec if i > 5]
print(d)

print("----------5--------------")
# 一些其他用法
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
result1 = [ i * j  for i in vec1 for j in vec2]
print(result1)
result2 = [ vec1[i] + vec2[i] for i in range(len(vec1))]
print(result2)

print("------------6------------")

str1 = [str(round(355/113, i)) for i in range(1, 6)]
print(str1)


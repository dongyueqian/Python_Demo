'''
break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。

break语句用在while和for循环中。

如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码
'''
i = 10
while i > 0:
    print(i)
    i -= 1
    if i == 6:
        break

print('********************')

for i in 'python':
    if i == 'h':
        break
    print(i)

print('======================================')
'''
continue 语句跳出本次循环，而break跳出整个循环。

continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。

continue语句用在while和for循环中'''

list = [1,2,3,4,5,6,7,8,9,10]
for i in list:
    if i % 2 == 0:
        continue
    print(i)
print('********************')

j = 10
while j >0:
    j = j - 1
    if j == 6:
        continue
    print(j)
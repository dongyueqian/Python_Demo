'''
for 循环和 while 循环
python中没有 do..while 循环
'''

'''
while 循环
while 语句用于循环执行程序，即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务。其基本形式为：
while 判断条件(condition)：
    执行语句(statements)……
'''
a = 1
while a < 10:
    print(a)
    a += 2

print('===============分割线==================')

numbers = [22,23,24,35,18,31,98,99]
even = []
old = []
while len(numbers)>0:
    number = numbers.pop()
    if (number % 2 == 0):
        even.append(number)
    else:
        old.append(number)
print(numbers)
print(even)
print(old)

print('===============分割线==================')

'''
while 语句时还有另外两个重要的命令 continue，break 来跳过循环，
continue 用于跳过该次循环，
break 则是用于退出循环，
此外"判断条件"还可以是个常值，
表示循环必定成立，具体用法如下：
'''
i = 0
while i < 10:
    i += 1
    if i % 2 > 0:   # 非双数时跳过输出
        continue
    print(i)        # 输出双数2、4、6、8、10
print('===============分割线==================')
j = 1
while 1:    # 循环条件为1必定成立
    print(j) # 输出1~10
    j += 1
    if j > 10: # 当i大于10时跳出循环
        break

print('===============分割线==================')

'''
无限循环
如果条件判断语句永远为 true，循环将会无限的执行下去
'''
# while True:
#     num = int(input('请输入一个数：'))
#     print('输入的数是：',num)

print('===============分割线==================')

'''
循环使用 else 语句
while … else 在循环条件为 false 时执行 else 语句块
'''
num = 1
while num <5:
    print(num,'小于5')
    num += 1
else:
    print(num,'不小于5')


'''
简单语句组
类似 if 语句的语法，如果你的 while 循环体中只有一条语句，你可以将该语句与while写在同一行中
'''
flag = 1
# while (flag): print('Given flag is really true!')

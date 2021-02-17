'''
打印实心正方形
'''
def zhengfangxing1(n):
    for j in range(n):
        print('*  ' * n,end="")
        print()

num1 = int(input('请输入一个数字：'))
print('打印一个实心正方形：',zhengfangxing1(num1))

'''
打印空心正方形
'''

def zhengfangxing2(n):
    for j in range(n):
        if (j == 0) or (j == n - 1) :
            print('*  '* n)  # *后面2个空格
        else:
            print("*  "+"   "*(n-2)+'*') #  三个空格


num1 = int(input('请输入一个数字：'))
print('打印一个空心正方形：',zhengfangxing2(num1))

'''
打印等腰直角三角形
'''
def triangle2(n):
    for j in range(n):
        print("*  " * j)

num2= int(input('请输入一个数字：'))
print('打印一个等腰直角三角形：',triangle2(num2))

'''
打印等腰三角形
'''
def triangle3(n):
    for i in range(n):
        for j in range(0, n-i):
            print(end=" ")
        for k in range(i * 2 + 1 ):
            print("*", end="")
        print()

num3= int(input('请输入一个数字：'))
print('打印一个等腰三角形：',triangle3(num3))

'''
打印菱形
'''
def lingxing(lines):
    if lines % 2 == 0:
        print('请输入奇数')
        import sys
        sys.exit(0)
    half_lines = lines // 2 + 1
    # print(half_lines)
    # 打印上半
    for i in range(half_lines):
        print(" " * (half_lines - i), end="")
        print("*" * (2 * i + 1))
    # 打印下半
    for i in range(half_lines - 1):
        print(" " * (i + 2), end="")
        print("*" * (lines - 2 - 2 * i))

lines = int(input('请输入一个数字：'))
print('打印一菱形：',lingxing(lines))

'''
打印空心菱形
'''
def kongxinlingxing(lines):
    if lines % 2 == 0:
        print('请输入奇数')
        import sys
        sys.exit(0)
    half_lines = lines // 2 + 1
    # print(half_lines)
    # 打印上半
    for i in range(half_lines):
        print(" " * (half_lines - i), end="")
        # print("*" * (2 * i + 1))
        if i == 0:
            print('*')
        else:
            print('*', end='')
            print(' ' * (2 * i - 1), end='')  # 打印空格的数量
            print('*')

    # 打印下半
    for i in range(half_lines - 1):
        print(" " * (i + 2), end="")
        # print("*" * (7 - 2 - 2 * i))
        if i == 2:
            print('*')
        else:
            print('*', end='')
            print(' ' * (3 - 2 * i), end='')
            print('*')
#
lines = int(input('请输入一个数字：'))
print('打印一空心菱形：',kongxinlingxing(lines))




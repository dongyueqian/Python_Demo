'''
打印实心正方形
'''
kongxin=chr(9711)
shixin=chr(9679)

def triangle1(n):
    for j in range(n):
        print(kongxin * n,end=" ")
        print()

num1 = int(input('请输入一个数字：'))
print('打印一个实心正方形：',triangle1(num1))

'''
打印等腰直角三角形
'''
def triangle2(n):
    for j in range(n):
        print(shixin * j)

num2= int(input('请输入一个数字：'))
print('打印一个等腰直角三角形：',triangle2(num2))






'''
用递归的方式来生成斐波那契数列

'''
def fibs(n):
    if n <= 1:
        return n
    else:
        return fibs(n-1)+fibs(n-2)
# fibs(0)
# print(fibs(3))
num = int(input('please input a num:'))
if num <= 1:
    print(fibs(num))
else:
    for i in range(num):
        print(fibs(i))
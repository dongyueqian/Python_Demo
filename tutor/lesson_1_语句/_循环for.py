'''
for循环可以遍历任何序列的项目，如一个列表或者一个字符串
for循环的语法格式如下：
for iterating_var in sequence:
   statements(s)
'''
namelist = ['lily','shaly','tom','jim','jiang']
for name in namelist:
    print(name)

for letter in 'python':
    print(letter)

print('===============分割线==================')

'''
通过序列索引迭代
另外一种执行循环的遍历方式是通过索引
 range返回一个序列的数
'''
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print('当前水果：',fruits[index])
print('再见👋😄')

print('===============分割线==================')

'''
循环使用 else 语句
在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，
else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样
'''

'''
实例：打印10～20之间的质数，不是质数的也打印并说明
质数：又称素数,指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。
'''
for num in range(10,20):
    for i in range(2,num):
        # print(num, i)
        if num % i == 0:
            j = num/i
            print('%d不是质数,%d = %d * %d ' % (num,num,i,j))
            break
    else:
        print('%d是质数' % num)

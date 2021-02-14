
'''
【1】
传不可变对象实例
通过 id() 函数来查看内存地址变化
'''
def change(a):
    print('这里是指函数change（1）的内存地址:',id(a))  # 指向的是同一个对象
    a = 10
    print('这里是指函数a = 10 的内存地址:',id(a))  # 一个新对象

a = 1
print('这里是指a = 1 的内存地址:',id(a))
change(a)

'''
【2】
传可变对象实例
可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了

传入函数的和在末尾添加新内容的对象用的是同一个引用
'''
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return
# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)
print("------------------------")

'''
【3】
关键字参数

关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。

使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值

函数参数的使用不需要使用指定顺序
'''
def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return
# 调用printinfo函数
printinfo(age=50, name="runoob")

print("------------------------")

'''
【4】
默认参数
调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值
'''
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return
# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")


print("============================")

'''
【5】
不定长参数
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名
语法：
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
   
加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
'''
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: x")
    print(arg1)
    print(vartuple)

# 调用printinfo 函数
printinfo('sd')
print("------------------------")
printinfo([1,2,3,4],9)
print("------------------------")
printinfo(70, 60, 50,'dskj',888)
printinfo('iid',9)
print("------------------------")

'''
【6】
还有一种就是参数带两个星号 **基本语法如下:
def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
   
加了两个星号 ** 的参数会以字典的形式导入
'''
def peopleinfo(arg1,**agr2):
    print(arg1)
    print(agr2)

peopleinfo(22,a = 10,b = 9)
peopleinfo([22],c = 10)
print("------------------------")

'''
【7】
声明函数时，参数中星号 * 可以单独出现,
如果单独出现星号 * 后的参数必须用关键字传入:c = 10
'''
def f(a,b,*,c):
    return a+b+c
l = f(1,2,c=4)
print(l)
print("------------------------")
'''
【8】
匿名函数
python 使用 lambda 来创建匿名函数。

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

lambda 函数的语法只包含一个语句：
    lambda [arg1 [,arg2,.....argn]]:expression
'''
sum = lambda agr1,arg2: agr1 * 1 +arg2 * 2
print(sum(2,3))
print("------------------------")
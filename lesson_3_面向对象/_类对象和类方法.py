'''
类对象支持两种操作：属性引用和实例化。

属性引用 使用和 Python 中所有的属性引用一样的标准语法：obj.name。

类对象创建后，类命名空间中所有的命名都是有效属性名。所以如果类定义是这样:
'''
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'

# 实例化类
# 创建了一个新的类实例并将该对象赋给局部变量 x，x 为空的对象
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i ：",x.i)
print("MyClass 类的方法 f ：",x.f())
print('=================================')
'''
构造方法
类有一个名为 __init__() 的特殊方法 ，叫构造方法

该方法在类实例化时会自动调用：
def __init__(self):
    self.data = []

⚠️self代表类的实例，而非类

__init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上
'''

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def test(self):
        print('这是一个测试方法1：',self.r)
        print('这是一个测试方法2：',self.i)

# y = Complex()  # 报错，必须要带参数
y = Complex(2,3)
print(y.r,y.i)
print(y.test())  #等于下面👇这句
print(Complex.test(y))

print('=================================')
'''
类的方法
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，
类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例
'''
class people:
    name = ''
    age = 0
    __weight = 0  # 私有属性 ，在类外部无法直接进行访问
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print(self.__weight)
        return "%s说,我%d岁了，体重%s斤!" % (self.name,self.age,self.__weight)

p = people('lily',4,20)
print(p.speak())
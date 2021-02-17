'''
动态编程语言 是 高级程序设计语言 的一个类别，在计算机科学领域已被广泛应用。
它是一类 在运行时可以改变其结构的语言 ：例如新的函数、对象、甚至代码可以被引进，
已有的函数可以被删除或是其他结构上的变化。动态语言目前非常具有活力
'''
'''
【一】
运行的过程中给对象绑定(添加)属性
'''
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person('haha',2)
print(p.age,p.name)
print('='*20)

'''
在这里，我们定义了1个类Person，在这个类里，定义了两个初始属性name和age，
但是人还有性别啊！如果这个类不是你写的是不是你会尝试访问性别这个属性呢？
'''
# print(p.sex) # 报错 'Person' object has no attribute 'sex'，我们定义的类里面没有sex这个属性
p.sex = 'girl'  # 动态给实例绑定属性
print(p.sex)
print('='*20)

'''
【二】
运行的过程中给类绑定(添加)属性
'''
p1 = Person('lily',10)
# 我们尝试打印p1.sex，发现报错，p1没有sex这个属性
# 给p这个实例绑定属性对p1这个实例不起作用
# print(p1.sex)  # 报错 'Person' object has no attribute 'sex'。所以我们要给所有的Person的实例加上 sex属性

# 直接给Person绑定属性
Person.sex = None  #给类Person添加一个属性
print(p1.sex) # 如果p1这个实例对象中没有sex属性的话，那么就会访问它的类属性
                # 可以看到没有出现异常
print('='*20)

'''
【三】
运行的过程中给类绑定(添加)方法
'''
class Bird(object):
    def __init__(self,wingsCount,legsCount,eyesCount):
        self.wingsCount = wingsCount
        self.legsCount = legsCount
        self.eyesCount = eyesCount
    def fly(self):
        print('This bird can fly!')

boli = Bird(2,2,2)
print('小鸟boli有%d只翅膀，有%d条腿，有%d只眼睛' % (boli.wingsCount,boli.legsCount,boli.eyesCount))

def run(self,speed):
    print('%d条腿的小鸟也会跑，跑的速度是%s m/s' % (self.legsCount,speed))

momo = Bird(3,3,3)
momo.fly()
# momo.run() # 报错，'Bird' object has no attribute 'run'
print('-'*20)
## 解决方法：给类添加方法
import types
# 通过MethodType方法给类绑定方法后
# run 就是Bird类的属性了
momo.run = types.MethodType(run,momo)
momo.run(10)
# 下面👇的代码意思是给momo这个实例增加了属性age，并赋值
momo.age = 30
print(momo.age)



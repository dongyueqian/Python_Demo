'''
元类：就是用来创建类的（东西）
创建类 就是为了创建类的实例对象（python中的类也是对象）
元类就是用来创建这些类（对象）的
⚠️元类就是类的类
可以通过检测__class__属性来验证：
'''
age = 50
print("age的数据类型：",age.__class__) # <class 'int'>
print(age.__class__.__class__)  # <class 'type'>
name = 'lily'
print("name的数据类型：",name.__class__) # <class 'str'>
print(name.__class__.__class__)  # <class 'type'>
class Bird(object):
    pass
b = Bird()
print("b的数据类型：",b.__class__) #  <class '__main__.Bird'>
print(b.__class__.__class__)   # <class 'type'>



print('='*50)
'''
【一】
类同样是对象

当执行下面的语句时，将在内存中创建一个对象，名字叫ObjectCreator
这个对象（类）自身拥有创建对象（类的实例）的能力
而这就是为什么它是类的原因。
但是，它（ObjectCreator）本质上仍然是个对象

你可以对它进行以下操作：
    1、可以把它做为参数在函数中进行传递
    2、可以给它增加属性
    3、可以copy它
    4、可以将它赋值给一个变量
'''
class ObjectCreator(object):
    pass

# my_object = ObjectCreator()
# print(my_object)  # 结果：<__main__.ObjectCreator object at 0x10d038358>
print(ObjectCreator) # 结果：<class '__main__.ObjectCreator'>
print(ObjectCreator())


#定义一个函数
def test(a):
    print(a)

print('把ObjectCreator做为参数在函数中进行传递:',end='')
test(ObjectCreator)

# hasattr(object,name)
# 判断一个对象里是否有name属性或者name方法，返回bool值
print('是否有name属性或者name方法：',hasattr(ObjectCreator,'get_name'))  # False

# 给ObjectCreator增加属性
ObjectCreator.get_name = 'lily'
print('是否有name属性或者name方法：',hasattr(ObjectCreator,'get_name'))  # True
print('直接调用ObjectCreator的属性：',ObjectCreator.get_name)

# 赋值给一个变量
objectCreatorMirror = ObjectCreator
print(objectCreatorMirror())

print('='*50)

'''
【二、】
动态创建类
'''
def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo  # 返回的是类，不是类的实例
    else:
        class Bar(object):
            pass
        return Bar

myClass = choose_class('foo')

# <class '__main__.choose_class.<locals>.Foo'>,返回的是类（对象），而不是类的实例
print(myClass)
# <__main__.choose_class.<locals>.Foo object at 0x10b1be710> 可以通过这个类创建实例，也就是对象
print(myClass())
print('='*50)

'''
【三】
动态创建类 升级
'''
print('动态创建类 升级')

class ObjectMethod(object):
    pass

print(type(1)) # 结果：<class 'int'>
print(type('1')) # 结果：<class 'str'>
print(type(ObjectMethod())) # 结果：<class '__main__.ObjectMethod'>
print('-'*50)

# type的格式
# type(类名，父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）（字典也可以为空）)
print('type说明')
myNewClass = type("ObjectMethod",(),{})

# 结果：<class '__main__.ObjectMethod'>，返回一个类对象
print(myNewClass)

# 结果：<__main__.ObjectMethod object at 0x110074780>，创建一个该类的实例
print(myNewClass())

print('='*50)

class Bird(object):
    singing = 'yingyingying~'

singingBird = Bird
print('原始的方式：',singingBird)
print('原始的方式：',singingBird.singing)
#上面申明类的方式和下面的通过type方式创建类的方式，是一样的
Bird = type("Bird",(),{"singing":"yingyingying~"})
print('type的方式：',Bird)
print('type的方式：',Bird.singing)
print('='*50)
'''
【四】
type方法继续讲解
定义了父类，又定义一个函数（方法）准备被子类来使用
通过type来实现子类
'''
print('type方法继续讲解～')
class Swim(object):
    swimming = "huahuahua～"

# class ChildClassSwim(Swim):  #子类
#     pass

def sportsman(self):
    return "我会游泳"

# my_swim = ChildClassSwim()
# print(my_swim.swimming)
print('*'*50)

# (Swim,)可以为空
ChildClassSwim2 = type('ChildClassSwim2',(Swim,),{"sportsman":sportsman}) #这一句等同上面对ChildClassSwim的定义
my_swim2 = ChildClassSwim2()
print(ChildClassSwim2)
print(my_swim2.sportsman)
print(my_swim2.sportsman())  # 结果：我会游泳
'''
动态语言：可以在运行的过程中，修改代码

静态语言：编译时已经确定好代码，运行过程中不能修改

如果我们想要限制实例的属性怎么办？比如，只允许对Person实例添加name和age属性。

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性

'''
class Person(object):
    __slots__ = ('name','age')

p = Person()
p.name = 'lily'
p.age = 20
print(p.name,p.age)

# p.sex = 'girl'
# print(p.sex) # 由于sex没有被放在 __slots__ 中，所以不能绑定 sex 属性
            # 给实例p绑定sex属性会报错 AttributeError: 'Person' object has no attribute 'sex'

'''
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
'''
class Test(Person):
    pass

t = Test()
t.sex = 'boy'  # 子类可以绑定属性
print(t.sex)
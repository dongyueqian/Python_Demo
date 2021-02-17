'''
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法
'''
class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类,继承父类
    def myMethod(self):  #重写父类方法
        print('调用子类方法')

#
# c = Child()  # 子类实例
# c.myMethod()  # 子类调用重写方法
# 用子类对象调用父类已被覆盖的方法
# super(Child,c).myMethod()


'''
super函数
'''
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aooaoao~')
            self.hungry = False
        else:
            print('No thanks')

class SongBird(Bird):
    def __init__(self):
        self.sound = 'Hahahaha~'
        # super(SongBird, self).__init__()
        super().__init__() # super函数
    def sing(self):
        print(self.sound)

sbird = SongBird()
print(sbird.sing())
print(sbird.sound)
print(sbird.eat())  #  用子类对象调用父类已被覆盖的方法
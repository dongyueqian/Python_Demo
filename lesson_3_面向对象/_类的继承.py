class people:
    name = ''
    age = 0
    _weight = 0  # 私有属性 ，在类外部无法直接进行访问
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self._weight = w

    def speak(self):
        return "%s说,我%d岁了，体重%s斤!" % (self.name,self.age,self._weight)

#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        # 调用父类的构造函数
        people.__init__(self,n,a,w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        return "%s说,我%d岁了，体重%s斤 ，读%d年级!" % (self.name,self.age,self._weight,self.grade)

xiaoming = student('小明',10,70,6)
print(xiaoming.speak())

print('=================================')

'''
多继承
'''
# 另一个类，多重继承之前的准备
class run:
    distance = ''
    def __init__(self,d):
        self.distance = d
    def running(self):
        return "我能跑 %s 米！" % self.distance

# xiaohong = run(800)
# print(xiaohong.running())
class demo(student,run):
    def __init__(self,n,a,w,g,d):
        student.__init__(self,n,a,w,g)
        run.__init__(self,d)

xiaogang = demo('小刚',13,100,8,900)
print(xiaogang.speak())
print(xiaogang.running())


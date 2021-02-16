'''
枚举的定义

首先，定义枚举要导入enum模块。
枚举定义用class关键字，继承Enum类。

⚠️ 枚举成员不能重复
'''
from enum import Enum
class Color(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7
# 上面的代码，我们定义了颜色的枚举Color.
# 颜色枚举有7个成员，分别是Color.red、Color.orange、Color.yellow等。
# 每一个成员都有它们各自名称和值，Color.red成员的名称是：red，值是：1。
# 每个成员的数据类型就是它所属的枚举。【*注：用class定义的类，实际上就是一种类型】

# 打印枚举成员的名字和值
print(Color.red.name)
print(Color.red.value)
# 通过序列号查找成员变量、名字和值
print(Color(2))
print(Color(2).name)
print(Color(2).value)
print('=='*10)

# 枚举支持迭代器，可以遍历枚举成员
print('遍历枚举成员：')
for item in Color:
    print(item)

print('=='*30)
'''
用于定义枚举类的class和定义类的class不同
下面的代码会报错
'''
# c = Color()

'''
默认情况下，不同成员的值是允许相同的
但两个相同值的成员，第2个成员的名字被视为第1个成员的别名
如果枚举中存在相同值的成员，在通过值获取枚举成员时，只能获取第1个成员

'''
class Color2(Enum):
    red = 1
    blue = 2
    black = 2

print(Color2(1))
print(Color2(2)) #可以获取
# print(Color2(3)) #报错
print('='*20)
'''
装饰器
如果要限制定义枚举时不能定义相同值的成员，
可以使用装饰器
需要导入unique模块
'''
from enum import Enum,unique
@unique
class Color3(Enum):
    red = 1
    blue = 2
    # black = 2 # 报错 ValueError: duplicate values found in <enum 'Color3'>: black -> blue
    black = 3
'''
没有限制定义相同值的成员时，
如果想把重复的成员遍历出来，
要用枚举的一个特殊属性 __members__
'''
class Color4(Enum):
    red = 1
    blue = 2
    black = 2
for item in Color4: # 打印不出black
    print(item.name)
print('-'*30)
print('特殊属性 __members__')
for item in Color4.__members__.items():
    print(item)
print('='*20)
'''
枚举成员比较
不能用< > <=等
'''
class Color5(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7

print(Color5.red is Color5.blue)
print(Color5.red is not Color5.blue)
print(Color5.red == Color5.blue)
print(Color5.red != Color5.blue)
print(Color5.red <= Color5.blue) # 报错
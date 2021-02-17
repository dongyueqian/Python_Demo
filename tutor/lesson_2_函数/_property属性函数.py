'''
学完面向对象后再学此节课程
'''
from decimal import Decimal

'''
property() 函数的作用是在新式类中返回属性值

以下是 property() 方法的语法:

class property([fget[, fset[, fdel[, doc]]]])

参数
fget -- 获取属性值的函数
fset -- 设置属性值的函数
fdel -- 删除属性值函数
doc -- 属性描述信息

返回值:
返回新式类属性。
'''
class Fees:
    def __init__(self):
        self.__fee = ''

    def get_fee(self):
        return self.__fee

    def set_fee(self,value):
        if isinstance(value,str):
            self.__fee = Decimal(value).quantize(Decimal('0.00')) # 保留2位小数
            print("1:",type(self.__fee))
        elif isinstance(value,Decimal):
            self.__fee = value
            print("2:", type(self.__fee))
        else:
            self.__fee = value
            print("3:",type(self.__fee))

    fee = property(get_fee,set_fee)


f = Fees()
print(f.get_fee())
print('-'*20)

f2 = Fees()
f2.set_fee('333.444')
print(f2.get_fee())
print('-'*20)

f3 = Fees()
f3.set_fee('7788.9999')
print(f3.get_fee())
# 定义了属性函数后，可直接通过类似属性设置属性值与获取属性值
# 上面的与下面👇这句一样
f3.fee = '100.999'
print(f3.fee)  #相当于调用了get_fee()

print('-'*20)
'''
用装饰器优化Fees类
'''
class Fees2:
    def __init__(self):
        self.__fee = ''

    @property
    def fee(self):
        return self.__fee
    @fee.setter
    def fee(self,value):
        if isinstance(value,str):
            self.__fee = Decimal(value).quantize(Decimal('0.00')) # 保留2位小数
            print("1:",type(self.__fee))
        elif isinstance(value,Decimal):
            self.__fee = value
            print("2:", type(self.__fee))
        else:
            self.__fee = value
            print("3:",type(self.__fee))
    # @fee.deleter
    # @fee.getter

f4 = Fees2()
f4.fee = 9999.9999
print(f4.fee)

f5 = Fees2()
f5.fee = '9999.9999'
print(f5.fee)
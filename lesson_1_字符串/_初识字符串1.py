'''

字符串格式化

左侧 % 右侧
左侧：放置一个字符串
右侧：放置希望被格式化的值

如果对应的值是多个，值应该放在元组里中


'''
list_num = 'Hello , My %s is dongyq , I am %d years old!'
values = ('name',15)
print(list_num % values)

print('***********分割线***********')

print('%s is girl,%s is boy,lily is %s' % ('lily','tom',15))
print('price of eggs is : $%d' % (50)) # 十进制
print('price of apples is : $%x' % (42)) # x 16进制

print('***********分割线***********')
'''
宽度与精度
10.2f :10表示宽度，. 后面的2表示精度
'''
from math import pi
print(pi)
print('pi : %f' % (pi))
print('pi : %10f' % pi )
print('pi : %10.2f' % pi )
print('pi : %.2f' % pi )

# 如果转化的是字符串，那么.后的数字就表示最大字段宽度
print('%.5s' % 'hauuhakjshdk   kjahskj khsjahkj')
print('%10.5s' % 'hauuhakjshdk   kjahskj khsjahkj')

# 如果是*，那精度会从元组中读取,第一个*表示宽度：10，第二个*表示精度：2
print('%*.*s' % (10,2,'hauuhakjshdk   kjahskj khsjahkj'))

print('%.*s' % (4,'djshjhsjdhkas'))

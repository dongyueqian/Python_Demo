import sys
# print(sys.path)
print(sys.argv)
for i in sys.path:
    print(i)


# 导入模块
import support
# 现在可以调用模块里包含的函数了
support.print_func('pppllll')
print('*'*80)

# 过滤点以__开头的（__开头的不是为模块外部使用而准备的）
print(dir(support))
d = [i for i in dir(support) if not i.startswith('__')]
print(d)

print('*'*80)

import copy

print(dir(copy))
print(copy.__all__)
c = [i for i in dir(copy) if not i.startswith('_')]
print(c)

print('*'*80)
help(copy.copy)
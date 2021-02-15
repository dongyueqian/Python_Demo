import sys
# print(sys.path)
print(sys.argv)
for i in sys.path:
    print(i)
print(sys.ps2)


# 导入模块
import support
# 现在可以调用模块里包含的函数了
support.print_func('pppllll')
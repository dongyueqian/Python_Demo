'''
os模块提供了很多跟操作系统相关联的函数
'''
import os
print('返回当前工作目录',os.getcwd())  #返回当前工作目录 /Users/dongyueqian/Documents/Python_lesson/Python_Demo/模块和标准库
# print(os.chdir('/Users/dongyueqian')) #修改当前的工作目录
# print('返回修改后的当前工作目录：',os.getcwd())  # 返回当前工作目录 /Users/dongyueqian
# os.system('mkdir today') # 指向该条代码后 会在目录/Users/dongyueqian 下新建一个today文件夹
print('*'*80)
'''
建议使用 "import os" 风格而非 "from os import *"。
这样可以保证随操作系统不同而有所变化的 os.open() 不会覆盖内置函数 open()。
在使用 os 这样的大型模块时内置的 dir() 和 help() 函数非常有用:
'''
print(dir(os)) #<returns a list of all module functions>
print(help(os.getcwdb))
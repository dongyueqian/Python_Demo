'''
在 Python 中，迭代器是一种非常好用的数据结构，
其最大的优势就是延迟生成，按需使用，从而大大提高程序的运行效率。
而 itertools 作为 Python 的内置模块，就为我们提供了一套非常有用的用于操作可迭代对象的函数。


⚠️ 无限循环迭代器只有在 for 循环中才会不断的生成元素，
如果只是创建一个迭代器对象，则不会事先生成无限个元素
'''

import itertools

'''
【一】、
count(start=0,step=1) 函数有两个参数，其中 step 是默认参数，可选的，默认值为 1。 
该函数返回一个新的迭代器，从 start 开始，返回以 step 为步长的均匀间隔的值。
'''
# for i in itertools.count(1,1):
#     print(i)  # 从1开始，步长为2，输出1，3，5，7，9.....无穷尽

'''
【二】、
cycle(iterable) 该函数会把接收到的序列无限重复下去。
注意，该函数可能需要相当大的辅助空间（取决于 iterable 的长度）。
'''
x = itertools.cycle('abc')
# for i in x:
#     print(i)   # 无限循环输出  a b c a b c.....

'''
【三】、
repeat(object, times) 该函数创建一个迭代器，不断的重复 object，
当然如果指定 times 的话，则只会重复 times 次
'''
# y = itertools.repeat('abc',3)
# for i in y:
#     print(i)    # 输出 abc abc abc


'''
【四】、
chain(*iterables) 该函数创建一个新的迭代器，
会将参数中的所有迭代器全包含进去。

'''
z = itertools.chain('abc','AbC')
# print(list(z))
# 或者如下👇
for i in z:
    print(i)

'''
【五】、
groupby(iterable, key=None) 分组函数，将 key 函数作用于序列的各个元素。
根据 key 函数的返回值将拥有相同返回值的元素分到一个新的迭代器。
类似于 SQL 中的 GROUP BY 操作，唯一不同的是该函数对序列的顺序有要求，
因为当 key 函数的返回值改变时，迭代器就会生成一个新的分组。
因此在使用该函数之前需要先使用同一个排序函数对该序列进行排序操作。
'''
# http://www.ityouknow.com/python/2019/10/23/python-itertools-039.html


'''
【六】、
'''


'''
【七】、
'''

'''
【八】、
'''

'''
【九】、
'''




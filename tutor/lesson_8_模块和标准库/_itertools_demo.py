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
y = itertools.repeat('abc',3)
for i in y:
    print(i)    # 输出 abc abc abc


'''
【四】、
chain(*iterables) 该函数创建一个新的迭代器，
会将参数中的所有迭代器全包含进去。

'''
# z = itertools.chain('abc','AbC')
# # print(list(z))
# # 或者如下👇
# for i in z:
#     print(i)

'''
【五】、
groupby(iterable, key=None) 分组函数，将 key 函数作用于序列的各个元素。
根据 key 函数的返回值将拥有相同返回值的元素分到一个新的迭代器。
类似于 SQL 中的 GROUP BY 操作，唯一不同的是该函数对序列的顺序有要求，
因为当 key 函数的返回值改变时，迭代器就会生成一个新的分组。
因此在使用该函数之前需要先使用同一个排序函数对该序列进行排序操作。
'''
# 案例1：根据日期字段对字典进行分组并且迭代访问

# from operator import itemgetter
# rows = [
#     {'address': '5412 N CLARK', 'date':'07/01/2020'},
#     {'address': '5222 N CLARK', 'date': '04/01/2020'},
#     {'address': '4531 E 58TH', 'date': '08/09/2020'},
#     {'address': '2367 W CHINA', 'date': '09/11/2020'},
#     {'address': '1100 E ADDSION', 'date': '05/01/2020'},
#     {'address': '5533 N REVENSWOOD', 'date': '10/01/2020'},
#     {'address': '4212 W APPLE', 'date': '03/01/2020'},
#     {'address': '1020 E MEITUAN', 'date': '02/28/2020'}
# ]
# # 对字典rows进行排序
# rows.sort(key=itemgetter('date'))
# # print(rows)
# for date,item in itertools.groupby(rows,key=itemgetter('date')):
#     print(date)
#     for i in item:
#         print(i)
#         print('='*30)


# 案例2：自定义一个排序函数 sortBy 将列表中的元素进行分组操作
# def sortBy(score):
#     if score > 80:
#         return 'A'
#     elif score > 60:
#         return 'B'
#     else:
#         return 'C'
#
# score = [81, 82, 84, 76, 64, 78, 59, 44, 55, 89]
# # 首先对score进行一下排序
# score = sorted(score,key=sortBy)   #没有这句的话，输出结果会把89单独分组
# for m,n in itertools.groupby(score,key=sortBy):
#     print(m,list(n))

'''
【六】
compress(data, selectors) 该函数功能很简单，
就是根据 selectors 中的值判断是否保留 data 中对应位置的值。
'''
# data = (81, 82, 84, 76, 64, 78)
# tf = (1,1,0,1,1,0)
# print(tuple(itertools.compress(data,tf)))

'''
【七】
dropwhile(predicate, iterable) 
使用时，你给它传递一个函数对象和一个可迭代对象。 
它会返回一个迭代器对象,丢弃原有序列中直到函数返回Flase之前的所有元素，然后返回后面所有元素
从 predicate 首次为 false 时开始迭代元素。

你想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们.

其他的案例：https://blog.csdn.net/weixin_43866211/article/details/101756115
'''
# lambda用法指路：/lesson_2_函数/_map函数.py
# x = itertools.dropwhile(lambda x: x < 5, [1,3,5,7,4,2,1])
# print(list(x))

'''
【八】
islice(iterable, start, stop[, step]) 对 iterable 进行切片操作。
从 start 开始到 stop 截止，同时支持以步长为 step 的跳跃。

'''
# m = '123456789'
# print(list(itertools.islice(m, 7)))  # 等于 print(list(m[:7]))
# print(list(itertools.islice(m, 2, 4))) # 等于 print(list(m[2:4]))
# print(list(itertools.islice(m, 2, None))) # 等于 print(list(m[2:]))
# print(list(itertools.islice(m, 0, None, 2)))  # 等于 print(list(m[0::2]))
# print('='*30)
# #跳过前3个元素的案例
# items = ['a', 'b', 'c', 1, 4, 10, 15]
# for i in itertools.islice(items,3,None):
#     print(i)





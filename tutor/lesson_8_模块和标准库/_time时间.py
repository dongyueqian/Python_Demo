'''
在python文档中，time是归类在常规操作系统服务中，
它提供的功能更加接近于操作系统层面。
其所能表述的日期范围被限定在1970-2038之间，
如果需要表述范围之外的日期，可能需要考虑使用datetime模块更好。

常用方法：

1、time.sleep(sec)：推迟指定时间sec后继续运行
2、time.localtime([sec])：将一个时间戳转化成一个当时时区的struct_time，
    如果sec参数未输入，则以当前时间为转化标准
3、time.strftime(format[,t])：将指定的struct_time（默认为当前时间），
    根据指定的格式化字符串输出。把一个代表时间的元组或者struct_time转化为格式化的时间字符串。
    如果t为指定，将传入time.localtime()。如果元组中任何一个元素越界，ValueError的错误将会被抛出
4、time.time()：返回当前时间的时间戳（以秒表示的浮点数）
5、time.mktime(t)：将一个struct_time转换为时间戳
6、time.gmtime([sec])：将一个时间戳转化为UTC时区（0时区）的struct_time
7、time.clock()：用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用
    第二次调用是自第一次调用以后到现在的运行时间
    ⚠️ Python 3.8 已移除 clock() 方法 可以使用 time.perf_counter() 或 time.process_time() 方法替代
8、time.asctime([t])把一个时间的元组或者struct_time表示为“Sun Jun 20 23:21:05 1993”，
    如果无参数，则会把time.localtime()作为参数传入
9、time.ctime([sec])：把一个时间戳转化为time.asctime()的形式，
    如果无参数或者为None时，则会把time.time()作为参数传入。
    它的作用相当于time.asctime(time.localtime(sec))
'''
import time

# time.struct_time(tm_year=2021, tm_mon=2, tm_mday=17, tm_hour=19,
# tm_min=41, tm_sec=57, tm_wday=2, tm_yday=48, tm_isdst=0)
print("本地时间为 :",time.localtime(time.time()))

# 2、time.localtime([sec])
# 结果：把时间戳1613562098格式化成struct_time形式：
# time.struct_time(tm_year=2021, tm_mon=2, tm_mday=17, tm_hour=19,
# tm_min=41, tm_sec=38, tm_wday=2, tm_yday=48, tm_isdst=0)
print('把时间戳1613562098格式化成struct_time形式：',time.localtime(1613562098))

# 3、time.strftime(format[,t])
# 把当前时间格式化成 2021-02-17 19:50:08 这种形式
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# 与上面的代码一样
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# 4、time.time()：返回当前时间的时间戳（以秒表示的浮点数）
print('返回当前时间的时间戳:',time.time())

# 5、time.mktime(t)：将一个struct_time转换为时间戳
# t -- 结构化的时间或者完整的9位元组元素
t = (2021, 2, 17, 20, 17, 25, 2, 48, 0)
print(time.mktime(t))

# 6、time.gmtime([sec])：将一个时间戳转化为UTC时区（0时区）的struct_time
print('把时间戳1613562098格式化成struct_time形式：',time.gmtime(1613563587.848999))

# 7、time.clock()
# time.perf_counter()  # 返回系统运行时间
# time.process_time()  # 返回进程运行时间
print('返回系统运行时间',time.perf_counter() )
print('返回当前的CPU时间(进程运行时间):',time.process_time())

# 8、time.asctime([t])
print(time.asctime(t))  # Wed Feb 17 20:17:25 2021
print(time.asctime(time.localtime()))  # 格式同上
print(time.asctime(time.localtime(1613562098))) # 格式同上

# 9 、time.ctime([sec])：把一个时间戳转化为time.asctime()的形式
print ("time.ctime() : %s" % time.ctime())
print ("time.ctime() : %s" % time.ctime(1613563587.848999))








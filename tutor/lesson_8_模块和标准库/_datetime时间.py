'''
2021年2月17日 周三

'''

from datetime import date,datetime
now = datetime.now()
print(now)   # 2021-02-17 19:23:40.964212
t = datetime.ctime(now)
print(t)    # Wed Feb 17 19:23:40 2021
print(datetime.date(now))   # 2021-02-17
print(now.year,now.month,now.day,now.hour,now.minute,now.second) # 2021 2 17 19 23 40

print('='*10)

# 02-17-21. 17 Feb 2021 is a Wednesday on the 17 day of February.
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

'''
datetime比time高级了不少，可以理解为datetime基于time进行了封装，提供了更多实用的函数，主要包含一下几类：

timedelta：主要用于计算时间跨度
tzinfo：时区相关
time：只关注时间
date：只关注日期
datetime：同时有时间和日期
在实际使用中，用得比较多的是datetime.datetime和datetime.timedelta，
另外两个datetime.date和datetime.time实际使用和datetime.datetime并无太大差别。
datetime.datetime 主要会有以下属性及常用方法：

datetime.year
datetime.month
datetime.day
datetime.hour
datetime.minute
datetime.second
datetime.microsecond
datetime.tzinfo()：时区
datetime.date()：返回date对象
datetime.time()：返回time对象
datetime.replace(name=value)
datetime.timetuple()：返回time.struct_time 对象
datetime.strftime(format)：按照format进行格式化输出


除了实例本身具有的方法,类本身也提供了很多好用的方法：

datetime.strptime(date_string,format)： 给定时间格式解析字符串
datetime.now([tz])：当前时间默认 localtime
datetime.today()：当前时间

'''


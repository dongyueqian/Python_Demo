'''
re.search 扫描整个字符串并返回第一个成功的匹配。
re.search(pattern, string, flags=0)
    pattern	匹配的正则表达式
    string	要匹配的字符串。
    flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
匹配成功re.search方法返回一个匹配的对象，否则返回None。

我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
    group(num=0)  匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
    groups()      返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
'''
import re
print(re.search('www', 'www.baidu.com').span())  # 在起始位置匹配
print(re.search('com', 'www.baidu.com'))  # 不在起始位置匹配

import re

line = "Cats are smarter than dogs"

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")

print('='*50)
'''
re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，
则匹配失败，函数返回 None，而 re.search 匹配整个字符串，直到找到一个匹配。
'''
import re

line = "Cats are smarter than dogs"

matchObj1 = re.match(r'dogs', line)
if matchObj1:
    print("match --> matchObj1.group() : ", matchObj1.group())
else:
    print("No match!!")

matchObj2 = re.search(r'dogs', line)
if matchObj2:
    print("search --> matchObj2.group() : ", matchObj2.group())
else:
    print("No match!!")
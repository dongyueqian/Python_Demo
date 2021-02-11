'''
 字典 get() 函数返回指定键的值。
dict.get(key, default=None)
key -- 字典中要查找的键。
default -- 如果指定的键不存在时，返回该默认值。
'''
dict = {'Name': 'Runoob', 'Age': 27}

print('Age 值为：%s' % dict.get('Age'))
print('Sex 值为：%s' % dict.get('Sex'))
print('School 值为：%s' % dict.get('School','beijing'))
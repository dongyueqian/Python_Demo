'''
字典 setdefault() 方法和 get()方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。

dict.setdefault(key, default=None)
    key -- 查找的键值。
    default -- 键不存在时，设置的默认键值。

如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None。
'''

dict = {'Name': 'Runoob', 'Age': 7}

print("Name 键的值为 : %s" % dict.setdefault('Name'))
print("Age 键的值为 : %s" % dict.setdefault('Age', None))
print("Sex 键的值为 : %s" % dict.setdefault('Sex', None))
print("新字典为：", dict)
'''
字典 pop() 方法删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
pop(key[,default]):
    key: 要删除的键值
    default: 如果没有 key，返回 default 值
返回被删除的值
'''
site= {'name': '哈哈酱', 'alexa': 10000, 'age': '22'}
pop_obj=site.pop('name')
print(pop_obj)
pop_obj=site.pop('','99') # 如果没有 key，返回 default 值
print(pop_obj)
print(site)

print('============================')

'''
字典 popitem() 方法随机返回并删除字典中的最后一对键和值。

如果字典已经为空，却调用了此方法，就报出KeyError异常。

无参数

返回一个键值对(key,value)形式，按照 LIFO（Last In First Out 后进先出法） 顺序规则，即最末尾的键值对。
'''
people_info = {'Tom':'9999999','Lily':'88888888','Saly':'93738434','jjjj':'2'}
pop_obj = people_info.popitem()
print(pop_obj)
print(people_info)
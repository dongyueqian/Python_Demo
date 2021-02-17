'''
字典 keys() 方法返回一个可迭代对象，可以使用 list() 来转换为列表
'''
people_info = {
    'Tom':{
        'sex':'男',
        'age': 14
    },
    'Lily':{
        'sex':'女',
        'age': 18
    },
    'Saly': {
        'sex': '女',
        'age': 17
    }
}
print(people_info.keys())

print(type(people_info.keys()))

print(list(people_info.keys()))
'''
字典通过{}包围
由键-值对组成
键是唯一的，值可以不唯一
字典里查看某个键的值是通过键的名称查找的，列表是通过索引
'''
phonebook1 = {"lily":"12345678","tom":"1361283909"}
print(phonebook1)
# print(phonebook[0])  #无法通过索引来查找数据
print(phonebook1["lily"])

print('**************分割线****************')

'''
dict函数
可以将列表或元组转化为字典
'''
phonebook2 = [["lily","12345678"],["tom","1361283909"]]
print(dict(phonebook2))
phonebook2 = [("lily","12345678"),["tom","1361283909"]]
print(dict(phonebook2))
phonebook2 = [("lily","12345678"),("tom","1361283909")]
print(dict(phonebook2))
phonebook2 = (("lily","12345678"),["tom","1361283909"])
print(dict(phonebook2))
phonebook2 = (("lily","12345678"),("tom","1361283909"))
print(dict(phonebook2))

print('**************分割线****************')
phonebook3 = {'lily': '12345678', 'tom': '1361283909','xixi':'7778888'}
print(len(phonebook3)) # 打印字典的长度
phonebook3['lily'] = '99999' # 更改字典中某个键的值
print(phonebook3)

del phonebook3['xixi']  # 删除键值对
print(phonebook3)

if 'xixi' in phonebook3:
    print(True)
else:
    print(False)
'''
字典 update() 函数把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里

dict.update(dict2)
    dict2 -- 添加到指定字典dict里的字典。

该方法没有任何返回值。

'''
dict = {'Name': 'Runoob', 'Age': 7}
dict2 = {'Sex': 'female'}

dict.update(dict2)
print("更新字典 dict : ", dict)
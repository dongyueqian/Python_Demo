'''
字典 clear() 函数用于删除字典内所有元素

dict.clear()
    无参数

该函数没有任何返回值。
'''
dict = {'Name': 'Zara', 'Age': 7}

print ("字典长度 : %d" %  len(dict))
dict.clear()
print ("字典删除后长度 : %d" %  len(dict))


print("===============================大分割线===============================")


x = {}
y = x    # 让y指向x
x['lily'] = '123'
print(x)
print(y)

print("**********分割线*************")
x = {}   #让x指向空，原来的地址内容不变，所以y的内容没有变化
print(x)
print(y)

print("**********分割线*************")

x1 = {}
y1 = x1
print(x1)
print(y1)
x1['tom'] = '88888'
print(x1)
print(y1)


print("**********字典的clear方法*************")
x1.clear()    # x1没有指向新的地址空间，而是把现在的clear了
print(x1)
print(y1)
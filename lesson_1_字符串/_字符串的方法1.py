'''
一、
find方法可以在一个字符串中查找子串，返回子串在父串中坐在位置最左端的索引
如果没找到，返回-1

'''
title = "My name is donghaha"
print(title.find('name'))
print(title.find('tom'))
print(title.find('is',7,19))

print('**********分割线*****************')

'''
二、
join方法：连接字符串
连接的序列元素必须是字符串
'''
student_name = ['I','am','a','Chinese','girl']
print(''.join(student_name))
print(' '.join(student_name))
print('-'.join(student_name))
nums = [1,2,3,4,5]
# print(''.join(nums)) #报错，连接的必须是字符串


#元组也可以哦
dirs = ('dongyq','python','demo')
print('/'.join(dirs))

print('**********分割线*****************')

'''
三、
split方法，将字符串切割为列表中的元素
默认split（）不加参数，是根据空格进行切分
'''
sentence = 'hello world!'
print(sentence.split())  #根据空格进行切分
nums = '1+2+3+4'
print(nums.split('+'))  #根据+号进行切分

print('**********分割线*****************')

'''
四、
lower方法
将字符串转化为小写字母版
'''
names = 'HELLO wORLd!'
print(names.lower())
names1 = ['lily','tom','shaly']
name2 = 'Shaly'
if name2.lower() in names1:
    print(True)
else:
    print(False)

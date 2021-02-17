'''
五、
replace方法:将指定字符串替换为目标字符串
replace(oldsub，newsub，n),n是指替换字符串的个数
'''
string_abc = "My name is donghaha,my mum's name is hahama,"
print(string_abc.replace('donghaha','dongyueqian'))
print(string_abc.replace('name','Name'))  # 第3个参数指定替换次数

print('**********分割线*****************')

'''
六、
strip() 去除字符串两边的空格
'''
lesson = 'Yuwen '
lessons = ['yuwen','shuxue','yingyu']
if lesson.lower().strip() in lessons:
    print(True)
else:
    print(False)


# 还可以去掉两边的*
print('*** lll * is njjkkk**'.strip('*'))

print('**********分割线*****************')

'''
七、
translate方法 ：接收1个参数，必须是字典类型（dict）
同时去掉多个字符，一般与maketrans函数结合使用
maketrans方法，接收2个参数，第一个是被转换的字符串，第二个是要转换的目标

列表：[], 元组：()， 字典：{}
'''
str = 'this is a string demo....'
instr = 'aeiou'
outstr = '12345'

transtr = str.maketrans(instr,outstr)
print(transtr)
print(str.translate(transtr))
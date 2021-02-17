'''
成员资格变量（in）
注意：input（）函数接收的是str类型
'''
student_info = [
    ['Lily',20],
    ['Tom',27],
    ['donghaha',18]
]
# name = input('请输入姓名：')
# age = int(input('请输入年龄：'))
# if [name,age] in student_info:
#     print('您查询的数据在列表中～')
# else:
#     print('您查询的数据不在列表中～')

'''
列表的长度、最大值、最小值
'''
nums = [0,1,3,4,5,9,8]
print('nums的长度：',len(nums))
print('nums的最大值：',max(nums))
print('nums的最小值：',min(nums))

strs = ['Alice','aly','Bob','shoy','bbu']
print('strs的长度：',len(strs))
print('strs的最大值：',max(strs))
print('strs的最小值：',min(strs))

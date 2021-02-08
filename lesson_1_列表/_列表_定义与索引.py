'''
键盘输入年、月、日，打印出格式化后的月-日-年：
输入：2021，2，6
输出：June-6th-2021

第几的表示方法：
1st，2nd，3rd，4～20th，21st，22nd，23rd，24～30th，31st
'''

months_list = ['January','February','March','April',
               'May','June','July','August','September',
               'October','November','December']

months_input = int(input('请输入月份（1～12）：'))
months = months_list[months_input-1]    #根据输入的月份找到对应的英文

days_end_list = ['st','nd','rd'] + 17 * ['th'] + ['st','nd','rd'] + 7 * ['th'] + ['st']
days_input = input('请输入日期（1～31）：')
days = days_input + days_end_list[int(days_input)-1]  # 根据输入的天数找到对应的结尾

years = int(input('请输入年份（纯数字）：'))

print('您输入的日期为：',months ,'-', days +'-',years)
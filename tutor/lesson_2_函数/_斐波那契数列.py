'''
写死
'''
# fibs1 = [0,1]
# for i in range(10):
#     fibs1.append(fibs1[-2] + fibs1[-1])
# print(fibs1)

'''
优化
'''
# fibs2 = [0,1]
# n = int(input('请输入一个数：'))
# for i in range(n):
#     fibs2.append(fibs2[-2] + fibs2[-1])
# print(fibs2)

'''
用函数实现
return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None
'''
def fibs(n):
    fibs3 = [0, 1]
    for i in range(n-2):
        fibs3.append(fibs3[-2] + fibs3[-1])
    return fibs3

print(fibs(10))
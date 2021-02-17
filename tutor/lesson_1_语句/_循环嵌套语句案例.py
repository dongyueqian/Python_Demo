'''
打印100以内的质数（素数）
'''
list = []
for i in range(2,100):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
    if(flag==0):
        print(i)
        list.append(i)
print(list)
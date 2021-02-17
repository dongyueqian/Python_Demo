'''
map() 函数会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列

语法：
map(function, iterable, ...)

参数：
function -- 函数
iterable -- 一个或多个序列
'''
def f(n):
    return n*n

n = [1,2,3,4]
print(list(map(f,n)))

# 结合匿名函数lambda使用
m = map(lambda x,y :x*2 + y ,[1,2,3,4,5,6],[1,2,3,3,2,1])
print(list(m))
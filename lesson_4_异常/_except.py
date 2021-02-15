'''
即便 Python 程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。
大多数的异常都不会被程序处理，都以错误信息的形式展现在这里
'''
# print(10 * (1/0) ) # ZeroDivisionError: division by zero。0 不能作为除数，触发异常
# print(4 + spam*3) # NameError: name 'spam' is not defined。spamspam 未定义，触发异常
# print('2' + 2) # TypeError: can only concatenate str (not "int") to str 。int 不能与 str 相加，触发异常

'''
异常处理：try/except
异常捕捉可以使用 try/except 语句
'''
# while True:
#     try:
#         x =  int(input("请输入一个数字: "))
#         break
#     except ValueError:
#         print("您输入的不是数字，请再次尝试输入！")

'''
try 语句按照如下方式工作；

首先，执行 try 子句（在关键字 try 和关键字 except 之间的语句）。

如果没有异常发生，忽略 except 子句，try 子句执行后结束。

如果在执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。

如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。

如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。
'''

'''
一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。

处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。

一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:

except (RuntimeError, TypeError, NameError):
    pass
'''
# while True:
#     try:
#         x =  int(input("请输入第一个数: "))
#         y =  int(input("请输入第二个数: "))
#         result = x / y
#         print(result)
#         break
#     # except ValueError:
#     #     print("您输入的不是数字，请再次尝试输入！")
#     # except ZeroDivisionError as z:
#     #     print('分母不能为0：',z)
#     except (RuntimeError, TypeError, NameError,ZeroDivisionError,ValueError) as e:
#         print(e)

'''
try/except...else
try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。
else 子句将在 try 子句没有发生任何异常的时候执行
'''
# while True:
#     try:
#         x =  int(input("请输入第一个数: "))
#         y =  int(input("请输入第二个数: "))
#         result = x / y
#     except ValueError as e:
#         print("您输入的不是数字，请再次尝试输入:",e)
#     except ZeroDivisionError as e:
#         print('分母不能为0：',e)
#     else:
#         print('结果是：',result)
#         print('正确')
#         break

'''
try-finally 语句无论是否发生异常都将执行最后的代码
'''
# while True:
#     try:
#         x =  int(input("请输入第一个数: "))
#         y =  int(input("请输入第二个数: "))
#         result = x / y
#     except ValueError as e:
#         print("您输入的不是数字，请再次尝试输入:",e)
#     except ZeroDivisionError as e:
#         print('分母不能为0：',e)
#     else:
#         print('结果是：',result)
#         print('正确')
#         break
#     finally:
#         print('这句话无论如何都会执行')


'''
抛出异常
Python 使用 raise 语句抛出一个指定的异常。

raise语法格式如下：

raise [Exception [, args [, traceback]]]
'''
#
# while True:
#     try:
#         x =  int(input("请输入第一个数: "))
#         y =  int(input("请输入第二个数: "))
#         if x < y:
#             raise Exception('x%s不能比%sy小，请重新输入!'%(x,y) )
#         else:
#             result = x / y
#     except ValueError as e:
#         print("您输入的不是数字，请再次尝试输入:",e)
#     except ZeroDivisionError as e:
#         print('分母不能为0：',e)
#     else:
#         print('结果是：',result)
#         print('正确')
#         break
#     finally:
#         print('这句话无论如何都会执行')


'''
raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。

如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出
'''
try:
    raise NameError('HiThere')
except NameError:
        print('An exception flew by!')
        raise
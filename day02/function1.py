#!/usr/bin/env python3
# 1. 调用函数

# Python内置了很多有用的函数，我们可以直接调用。
# 要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。

# 也可以在交互式命令行通过help(abs)查看abs函数的帮助信息。

# 1) 调用abs函数：
print(abs(100))
print(abs(-20))
print(abs(12.34))

# 2) 而max函数max()可以接收任意多个参数，并返回最大的那个：
print(max(1, 2))
print(max(2, 3, 1, -5))


# 2. 数据类型转换
# Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

fn = abs # 变量fn指向abs函数
print(fn(-1)) # 所以也可以通过a调用abs函数


# 小结

# 调用Python的函数，需要根据函数定义，传入正确的参数。如果函数调用出错，一定要学会看错误信息，所以英文很重要！

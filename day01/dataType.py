#!/usr/bin/env python3
# 数据类型和变量
# 数据类型
# 在Python中，能够直接处理的数据类型有以下几种：

# 1.整数
# Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样，例如：1，100，-8080，0，等等。
# 计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2，等等。

# 2.浮点数
# 浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的。如：1.23e9，或者12.3e8

# 整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），
# 而浮点数运算则可能会有四舍五入的误差。

# 3.字符串
# 字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等。
# 请注意，''或""本身只是一种表示方式，不是字符串的一部分，因此，字符串'abc'只有a，b，c这3个字符。
# 如果'本身也是一个字符，那就可以用""括起来

# 如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，比如：
# 'I\'m \"OK\"!'

# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\，
print('I\' ok.')
print('i\'m learning\nPython')
print('\\\n\\')

# 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
print('\\\t\\')
print(r'\\\t\\')

# 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''line1
line2
line3
''')

# 布尔值
# 布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False
# 在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来：
print(True)
print(False)
print(3 > 2)
print(3 > 5)

# 布尔值可以用and、or和not运算。

# 1）and运算是与运算，只有所有都为True，and运算结果才是True：
print('and 运算符')
print(True and True)
print(True and False)
print(False and False)
print(5 > 3 and 3 > 1)

# 2）or运算是或运算，只要其中有一个为True，or运算结果就是True：
print('or 运算符')
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(5 > 3 or 1 > 3)

# not运算是非运算，它是一个单目运算符，把True变成False，False变成True：
print('not 运算符')
print(not True)
print(not False)
print(not 1 > 2)

# 布尔值经常用在条件判断中，比如：
age = 19
if age >= 18:
    print('adult')
else:
    print('teenager')

# 空值
# 空值是Python里一个特殊的值，用None表示。
# None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
# 此外，Python还提供了列表、字典等多种数据类型，还允许创建自定义数据类型


# 变量     



# 字符串和编码

# 1.字符编码
# 字符串也是一种数据类型，但是，字符串比较特殊的是还有一个编码问题。
# ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节。

# 1) 字母A用ASCII编码是十进制的65，二进制的01000001；
# 2) 字符0用ASCII编码是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的；
# 3) 汉字中已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制的01001110 00101101。


# 搞清楚了ASCII、Unicode和UTF-8的关系，我们就可以总结一下现在计算机系统通用的字符编码工作方式：
# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
# 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：


# 2.Python的字符串
# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言，例如：
print('包含中文的str')

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A'))
# 65
print(ord('中'))
# 20013
print(chr(66))
# 'B'
print(chr(25991))
# '文'
# 如果知道字符的整数编码，还可以用十六进制这么写str：
print('\u4e2d\u6587')
# '中文'
# 两种写法完全是等价的。


# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> '中文'.encode('ascii') # 报错，超出了ASCII编码的范围

# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。
# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
>>> b'ABC'.decode('ascii')
'ABC'
>>>  b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'

# 要计算str包含多少个字符，可以用len()函数：
print(len('ABC'))
# 3
print(len('中文'))
# 2

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
>>> len(b'ABC')
3
>>> len(b'\xe4\xb8\xad\xe6\x96\x87')
6
>>> len('中文'.encode('utf-8'))
6
# 可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。

# 在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。

# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。


# 3.格式化
# 最后一个常见的问题是如何输出格式化的字符串。我们经常会输出类似'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串，
# 而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式。

# 在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：
>>> 'Hello, %s' % 'world'
'Hello, world'
>>> 'Hi, %s, you have $%d.' % ('Michael', 100000)
'Hi, Michael, you have $100000'

# %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，
# 有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。

# 常见的占位符有：
%d 整数
%f 浮点数
%s 字符串
%x 十六进制整数

# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
>>> 'Age: %s. Gender: %s' % (25, True)
'Age: 25. Gender: True'

# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
>>> 'growth rate: %d %%' % 7
'growth rate: 7 %'
# 其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
>>> '%2d-%02d' % (3, 1)
' 3-01'
>>> '%.2f' % 3.1415926
'3.14'

# 小结

# Python 3的字符串使用Unicode，直接支持多语言。
# str和bytes互相转换时，需要指定编码。最常用的编码是UTF-8。Python当然也支持其他编码方式，比如把Unicode编码成GB2312：
>>> '中文'.encode('gb2312')
b'\xd6\xd0\xce\xc4'
# 但这种方式纯属自找麻烦，如果没有特殊业务要求，请牢记仅使用UTF-8编码。




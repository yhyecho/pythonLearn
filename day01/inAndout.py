#!/usr/bin/env python3
# 输入和输出

# 输出
print('hello world')

print('The quick brown for', 'jumps over', 'the lazy dog')
# print()会依次打印每个字符串，遇到逗号“,”会输出一个空格，因此，输出的字符串是这样拼起来的

print('200 + 100 =', 200 + 100)

# 输入
# Python提供了一个input()，可以让用户输入字符串，并存放到一个变量里。
# >>> name = input()
# Michael

# 可以直接输入name查看变量内容：
# >>> name
# 'Michael'

name = input('please enter your name: ')
print('hello,', name)

# 每次运行该程序，根据用户输入的不同，输出结果也会不同。
# 在命令行下，输入和输出就是这么简单。

# 总结
# 输入是Input，输出是Output，因此，我们把输入输出统称为Input/Output，或者简写为IO。
# input()和print()是在命令行下面最基本的输入和输出

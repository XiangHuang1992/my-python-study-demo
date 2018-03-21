#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""删除字符和字符串
字符串是不可变的！所以不能仅仅删除一个字符串里的某个字符，能做的只能是清空一个字符串，或者是把剔除了不需要的部分后的字符串重新组合起来形成一个新串。
也可以通过赋值一个空串或者使用del语句来删除
"""


aString = 'hello world'
print('切片前的aString：', aString)
aString = aString[:3] + aString[4:]
print('切片后的aString：', aString)
aString = ''
print('aString：', aString)
del aString
"""输出结果
切片前的aString： hello world
切片后的aString： helo world
aString： 
"""

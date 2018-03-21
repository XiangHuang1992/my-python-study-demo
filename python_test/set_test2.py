#!/usr/bin/env python
# -*- coding=utf-8 -*-

s = set('huangxiang')

print('s中包含h:', 'h' in s)
print('s中不包含g:', 'g' not in s)

for i in s:  # for循环遍历集合元素
    print(i)

"""输出结果
s中包含h: True
s中不包含g: False
h
a
x
g
n
u
i
"""

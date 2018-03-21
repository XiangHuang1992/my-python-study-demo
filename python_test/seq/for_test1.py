#!/usr/bin/env python
# -*- coding=utf-8 -*-

Names = 'huangxiang'

for name in Names:
    print('current name is:', name)

nameList = ['huangxiang', 'zhangjun', 'linaying']

"""通过序列项迭代"""
for eachName in nameList:
    print('current name is:', eachName)

"""通过序列索引迭代
使用内建函数len()获取序列长度，使用range()创建了迭代序列。
"""
for nameIndex in range(len(nameList)):
    print('current name is:', nameList[nameIndex])

"""使用内建的enumerate()函数
"""
for i, eachName in enumerate(nameList):
    print("%d %s" % (i+1, eachName))

"""输出结果
current name is: h
current name is: u
current name is: a
current name is: n
current name is: g
current name is: x
current name is: i
current name is: a
current name is: n
current name is: g
current name is: huangxiang
current name is: zhangjun
current name is: linaying
current name is: huangxiang
current name is: zhangjun
current name is: linaying
1 huangxiang
2 zhangjun
3 linaying
"""

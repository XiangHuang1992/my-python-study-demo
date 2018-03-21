#!/usr/bin/env python
# -*- coding=utf-8 -*-
print('*******************创建tuple************************8')
aTuple = (123, 'huang', ['huang', 'xiang'], 4.56)
bTuple = (None, 'something here')
print(aTuple)
print(bTuple)
print(tuple('huangxiang'))  # 使用工厂方法创建tuple
print('*******************访问tuple中的值************************8')
print(aTuple[1:3])
print(aTuple[:3])
print(aTuple[2][1])
print('*******************更新tuple************************8')
aTuple = aTuple[0], aTuple[1], aTuple[2]
print(aTuple)
print('*******************移除tuple的元素或其本身************************8')
del aTuple
#print(aTuple)

"""输出结果
*******************创建tuple************************8
(123, 'huang', ['huang', 'xiang'], 4.56)
(None, 'something here')
('h', 'u', 'a', 'n', 'g', 'x', 'i', 'a', 'n', 'g')
*******************访问tuple中的值************************8
('huang', ['huang', 'xiang'])
(123, 'huang', ['huang', 'xiang'])
xiang
*******************更新tuple************************8
(123, 'huang', ['huang', 'xiang'])
*******************移除tuple的元素或其本身************************8
Traceback (most recent call last):
  File "/Users/ferdinand/my-python-study-demo/python_test/seq/tump_test1.py", line 18, in <module>
    print(aTuple)
NameError: name 'aTuple' is not defined

"""

#!/usr/bin/env python
# -*- coding=utf-8 -*-

# 创建list
print('*******************创建list************************8')
aList = [123, 'huang', 4.56, ['abc', 'def']]
bList = [None, 'hahah']

print(aList)
print(bList)

cList = []
print(cList)
print(list('huang'))  # 使用工厂方法创建

# 访问list中的值
print('*******************访问list中的值************************8')
print(aList[0])
print(aList[1:4])
print(aList[:3])
print(aList[3][1])
# 更新list
print('*******************更新list************************8')
aList[2] = 'new'
aList.append('something new ')
print('更新后的aList:', aList)
# 删除list或list本身
print('*******************删除list或本身************************8')
del aList[1]
print('删除后的aList：', aList)
aList.remove(123)
print('删除huang后的aList：', aList)
del aList  # 完全移除aList

"""输出结果
*******************创建list************************8
[123, 'huang', 4.56, ['abc', 'def']]
[None, 'hahah']
[]
['h', 'u', 'a', 'n', 'g']
*******************访问list中的值************************8
123
['huang', 4.56, ['abc', 'def']]
[123, 'huang', 4.56]
def
*******************更新list************************8
更新后的aList: [123, 'huang', 'new', ['abc', 'def'], 'something new ']
*******************删除list或本身************************8
删除后的aList： [123, 'new', ['abc', 'def'], 'something new ']
删除huang后的aList： ['new', ['abc', 'def'], 'something new ']
"""


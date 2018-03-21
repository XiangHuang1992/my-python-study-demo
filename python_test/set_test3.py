#!/usr/bin/env python
# -*- coding=utf-8 -*-

s = set('huangxiang')
t = set('huang')

print('s是t的子集：', s.issubset(t))
print('s是t的超集：', s.issuperset(t)) 
print('s和t的公共集：', s.union(t))   # 去除相同元素之后两个集合的元素集
print('s和t的交集：', s.intersection(t))  # 两个集合的交集
print('s和t不同的元素：', s.difference(t)) # 去除重复元素之后两个集合不同的元素集合
print(s.symmetric_difference(t))

# 使用in not in 判断元素是否在集合内
print('h在s中', 'h' in s)
print('a不在s中', 'a' not in s)

print('s==t:', s == t)

"""输出结果
s是t的子集： False
s是t的超集： True
s和t的公共集： {'i', 'x', 'u', 'a', 'n', 'g', 'h'}
s和t的交集： {'u', 'a', 'n', 'g', 'h'}
s和t不同的元素： {'i', 'x'}
{'i', 'x'}
h在s中 True
a不在s中 False
s==t: False
"""
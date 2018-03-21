#!/usr/bin/env python
# -*- coding=utf-8 -*-

s = set('huangxiang')
print('更新前的集合s：', s)

s.add('q')
print('添加q后的集合s：', s)

s.update('ufo')
print('添加ufo后的集合s：', s)

s.remove('h')
print('删除h后的集合s：', s)

s -= set('huangxiang')
print('删除huangxiang后的集合s：', s)

t = frozenset('xiang')  # 不可变集合不能修改，否则引发异常
# t.add('s')  # AttributeError: 'frozenset' object has no attribute 'add' 

"""输出结果
更新前的集合s： {'x', 'u', 'a', 'g', 'n', 'i', 'h'}
添加q后的集合s： {'x', 'u', 'a', 'g', 'n', 'i', 'h', 'q'}
添加ufo后的集合s： {'x', 'u', 'o', 'f', 'a', 'g', 'n', 'i', 'h', 'q'}
删除h后的集合s： {'x', 'u', 'o', 'f', 'a', 'g', 'n', 'i', 'q'}
删除huangxiang后的集合s： {'o', 'f', 'q'}
"""

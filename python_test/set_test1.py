#!/usr/bin/env python
# -*- coding=utf-8 -*-

s = set('huangxiang')

print('s=', s)

t = frozenset('huangxiang')

print('t= ', t)

print('type(s):', type(s))
print('type(t)', type(t))
print('len(s)=', len(s))
print('len(t)=', len(t))

"""输出结果：
s= {'i', 'g', 'x', 'a', 'h', 'u', 'n'}
t=  frozenset({'i', 'g', 'x', 'a', 'h', 'u', 'n'})
type(s): <class 'set'>
type(t) <class 'frozenset'>
len(s)= 7
len(t)= 7
"""

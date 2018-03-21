#!/usr/bin/env python
# -*- coding=utf-8 -*-
dict1 = {'sex': 'male'}
dict2 = {'name': 'huangxiang', 'age': '25'}

print('删除前的dict1:', dict1)

print('删除前的dict2:', dict2)

del dict2['name']

print('删除后的dict2:', dict2)

dict2.pop('age')

print('删除后的dict2:', dict2)

dict2.clear()   # 删除整个字典的元素

del dict1   # 删除整个字典
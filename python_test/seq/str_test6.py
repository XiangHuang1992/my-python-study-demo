#!/usr/bin/env python
# -*- coding=utf-8 -*-

import string

# 成员操作符实例
print('bc' in 'abc')
print('n' in 'abcd')
print('nm' not in 'abcd')

print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.ascii_letters)
print(string.digits)

# 连接符实例

print('huang' + 'xiang')
print('huang' + '' + 'xiang')

# 普通字符串转换成unicode字符串
print('huang' + u'' + 'xiang' + u'!')

# 重复操作符
print('huang' * 3)
print('*' * 40)
"""输出结果
True
False
True
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
huangxiang
huangxiang
huangxiang!
huanghuanghuang
****************************************
"""

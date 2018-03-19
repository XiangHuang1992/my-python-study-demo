# _*_ coding: utf-8 _*_

u"""创建字典."""

dict1 = {}
dict2 = {'name': 'huangxiang', 'age': '21'}

print(dict1, dict2)

dict3 = dict((['x', 1], ['y', 2]))

print(dict3)

dict4 = {}.fromkeys(('x', 'y'), (1, 2))

print(dict4)
print(dict4.keys())
print(dict4.items())
print(len(dict4))
print(dict4['x'])
print(iter(dict4.keys()))
dict3.clear()
print(dict3)
print(dict4.values())

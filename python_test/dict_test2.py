# _*_ coding: utf-8 _*_

u"""访问字典的值."""

dict1 = {}
dict2 = {'name': 'huangxiang', 'age': '25'}

for key in dict2.keys():  # 通过查询键来遍历字典
    print('key=%s, value=%s' % (key, dict2[key]))

for key in dict2:  # 使用for循环遍历字典
    print('key=%s, value=%s' % (key, dict2[key]))

print(dict2['name'])  # 获取字典中某个元素的值
print('server' in dict2)  # 查看字典中是否有'server'键对应的值
print('name' in dict2)

u""" 输出结果
key=name, value=huangxiang
key=age, value=25
key=name, value=huangxiang
key=age, value=25
huangxiang
False
True
"""

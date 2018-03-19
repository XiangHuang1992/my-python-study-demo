# _*_ coding: utf-8 _*_

u"""更新字典的值."""

dict1 = {}
dict2 = {'name': 'huangxiang', 'age': '25'}

print('更新前的dict：', dict2)


dict2['name'] = 'hujinli'  # 更新已有条目
dict2['age'] = '26'  # 更新已有条目
dict2['sex'] = 'male'  # 增加新条目

print('更新后的dict:', dict2)



u"""输出结果
更新前的dict： {'name': 'huangxiang', 'age': '25'}
更新后的dict: {'name': 'hujinli', 'age': '26', 'sex': 'male'}
"""

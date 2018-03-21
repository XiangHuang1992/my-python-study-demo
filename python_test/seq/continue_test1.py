#!/usr/bin/env python
# -*- coding=utf-8 -*-

valid = False
count = 3
passwdList = ['123', '134', '445']

while count > 0:
    pwdInput = input('请输入密码：')
    for eachPwd in passwdList:
        if pwdInput == eachPwd:
            valid = True
            break
    if not valid:
        print('invalid input')
        count -= 1
        continue
    else:
        break
     
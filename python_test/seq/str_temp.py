#!/usr/bin/env python
# -*- coding=utf-8 -*-

from string import Template
s = Template('$who likes $what')
print(s.substitute(who='tim', what='kung pao'))
d = dict(who='tim')
print(Template('$who likes $what').safe_substitute(d))

"""输出结果
tim likes kung pao
tim likes $what
"""

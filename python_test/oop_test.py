# -*- coding: utf-8 -*-
u"""添加新的书类型."""


class AddBookEntry(object):
    """docstring for AddB o okEntry."""

    def __init__(self, nm, ph):
        u"""初始化."""
        self.name = nm
        self.phone = ph
        print ('Created instance for:', self.name)

    def updatePhone(self, newPh):
        u"""更新手机号码的方法."""
        self.phone = newPh
        print ('Update phone# for:', self.name)

# _*_ coding: utf-8 _*_

"""documentation."""

import sys


class Parent:   # 定义父类
    """parent."""

    def parentMethod(self):
        """parentMethod."""
        print('calling parent method')


class Child(Parent):
    """childMethod."""

    def childMethod(self):
        """childMethod."""
        print('calling child method')


print(Parent.__base__)

c = Parent()
print(c)

print(sys.version)

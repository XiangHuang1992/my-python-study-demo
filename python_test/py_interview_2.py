# -*- coding: utf-8 -*-

"""
@staticmethod and @classmethod

python当中有三个方法：静态方法（staticmethod）类方法（classmethod）和实例方法
"""

def foo(x):
    print("executing foo(%s)" % (x))

class A(object):
    def foo(self,x):
        print("executing foo(%s, %s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s, %s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)

a = A()
a.foo(6)
a.class_foo(6)
a.static_foo(6)
foo(6)

#A.foo(6)
A.static_foo(6)
A.class_foo(6)


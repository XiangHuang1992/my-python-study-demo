# -*- coding: utf-8 -*-
"""
类变量和实例变量
类变量是可在类的所有实例之间共享的值，也就是说，它不是单独分配给每个实例的。
实例变量是实例化之后每个实例单独拥有的变量。
"""


class Test(object):
    num_of_instance = 0

    def __init__(self, name):
        self.name = name
        Test.num_of_instance += 1


if __name__ == "__main__":
    print(Test.num_of_instance)
    t1 = Test('jack')

    print(Test.num_of_instance)

    t2 = Test('ferdinand')
    print(Test.num_of_instance)

    print(t1.name, t1.num_of_instance)
    print(t2.name, t2.num_of_instance)

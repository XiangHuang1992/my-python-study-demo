# -*- coding: utf-8 -*-

a = 1
def fun(a):
   print("func_in", id(a))  # func_in 4362918912
   a = 2
   print("re_point", id(a), id(2)) # re_point 4501539872 4501539872

fun(a)
print(a) # 1

#a = []
#def fun(a):
#    a.append(1)

#fun(a)
#print(a)

"""
所有的变量都可以理解为是内存中一个对象的引用。和c中的void*有点类似。
在Python中，strings，tuples，和numbers都是不可更改的对象。而list，dict，set是可修改对象。

当一个引用的传递给函数的时候，函数自动复制一份引用。这个函数里的引用和外面的引用没有任何关系。
所以在第一个例子当中，函数把引用指向了一个不可变对象。当函数返回的时候，外面的引用没有任何感觉。返回结果依然是1.
而第二个例子则不一样，第二个例子函数内的引用是可变对象。对它的操作实际上是在内存当中进行修改。
""" 

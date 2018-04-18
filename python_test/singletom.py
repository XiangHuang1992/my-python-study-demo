"""
单例模式是一种常用的软件设计模式。在它的核心结构中只包含一个被称为单例类的特殊类。通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资源。如果希望在系统中某个类的对象只能存在一个，单例模式是最好的解决方案。

__new__()在__init__()之前被调用，用于生成实例对象。利用这个方法和类的属性的特点可以实现设计模式的单例模式。单例模式是指创建唯一对象，单例模式设计的类只能实例 这个绝对常考啊.绝对要记住1~2个方法,当时面试官是让手写的.
"""

# 使用__new__方法

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1

# 共享属性

# 创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法.

class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob

class MyClass2(Borg):
    a = 1

# 装饰器版本
def singleton(cls, *args, **kw):
    instance = {}
    def getInstance():
        if cls not in instance:
            instance[cls] = cls(*arg, **kw)
        return instance[cls]
    return getInstance

@singleton
class MyClass3:
    pass

# import方法
class My_Singleton(object):
    def foo(self):
        pass
my_singleton = My_Singleton()

from my_singleton import my_singleton

my_singleton.foo()

# 使用元类
class Singleton3(type):
    _instance = {}
    def __call__(cls, *args, **kw):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton3, cls).__call__(*args, **kw)
        return cls._instance[cls]

class MyClass4(metaclass=Singleton3):
    pass

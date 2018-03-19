class TestStaticMethod:
    # def foo():
    #     print('calling static method foo()')
    #
    # foo = staticmethod(foo)
    @staticmethod
    def foo():
        print('calling static method foo()')


class TestClassMethod:
    # def foo(cls):
    #     print('calling class method foo()', cls.__name__)
    #     print('foo() is part of class:', cls.__name__)
    #
    # foo = classmethod(foo)
    @classmethod
    def foo(cls):
        print('calling class method foo()')
        print('foo() is part of class:', cls.__name__)

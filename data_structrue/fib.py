"""
斐波拉契问题：F(0)=0,F(1)=1,F(n) = F(n-1)+ F(n-2) (n>2,n∈N*)
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个n级台阶总共有多少种跳法。
"""


def moeo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@moeo
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(10))

# fib2  = lambda n: n if n <= 2 else fib(n-1) + fib(n-2)

def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b


print(fib2(10))

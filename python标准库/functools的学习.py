# partial方法: 偏对象, 将一个函数copy给另一个函数, 可以改变形参. 返回的是一个可调用对象

import functools


def my_func(a, b=2):
    """my_func's doc"""
    print("{}-----{}".format(a, b))

if __name__ == '__main__':
    p1 = functools.partial(my_func, "para_a", b="para_b")
    p1()
    print(my_func)
    print(p1)

    print(my_func.__name__)
    print(p1.func)
    print(p1.args)
    print(p1.keywords)


# partial返回的对象没有原方法的__name__和__doc__, 可以用update_wrapper方法将原方法的属性复制或添加到partial对象
print('-' * 40)
functools.update_wrapper(p1, my_func)
print(p1.__name__)
print(p1.__doc__)


# partial可以对类和可调用对象使用.
print('-' * 40)


class MyClass:
    def __init__(self, a, b):
        print(a)
        print(b)

    def __call__(self, c, d):
        print("call", (self, c, d))


o = MyClass(a=1, b=2)
o(c=3, d=4)
p3 = functools.partial(MyClass, a=10, b=20)
p3()
p4 = functools.partial(o, 30, d=40)
p4()


# 装饰器, 如果不用wraps装饰, 转换后的函数会有「裸」函数的属性.
print('-' * 40)


def simple_decorator(f):
    @functools.wraps(f)
    def decorated(a="decorated", b=1):
        print('do something')
        return f(a, b=b)
    return decorated


@simple_decorator
def decorated_myfunc(a, b):
    print('qwertyuiop')
    return


decorated_myfunc()

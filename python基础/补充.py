# -*- coding: utf-8 -*-
# author: Luke
# 1. 冻结集合
l = [1,2,3,4,1,2,4]
fz = frozenset(l)
print(fz)



def multipliers():
    return [lambda x: x * i for i in range(4)]


print([m(2) for m in multipliers()])

# 后面的四个都正常，关于第一个，我只想说，匿名函数闭包生成器？劳资不会！！！

# 好像是这么回事，lambda 闭包只有在调用匿名函数的时候，才会取出里面的内容

# 上面执行顺序，先生成四个匿名函数，然后传入形参x为 2 调用 4个匿名函数，匿名函数调用时 i 的 值已经为 3 了！！！

def multipliers():
    return [lambda x, i=i: i * x for i in range(4)]

print([m(2) for m in multipliers()])


def multipliers():
    for i in range(4):
        yield  lambda x: x * i

print([m(2) for m in multipliers()])

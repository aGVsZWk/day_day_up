# 1--函数相关的语句和表达式
# myfunc('spam')      # 函数调用
# def myfunc():       # 函数定义
# return None         # 函数返回值
# global a            # 全局变量
# nonlocal a           # 在函数或其他作用域中使用外层(非全局)变量
# yield x             # 生成器函数返回
# lambda              # 匿名函数





# 2--python函数变量名解析: LEGB原则, 即:
"""
local(function)--> encloseing function locals --> global(module) --> build-in(python)
说明: 以下边的函数maker为例, 则相对于action而言, X为Local, N为Encloseing


局部变量-->封闭函数局部变量-->全局变量-->内置变量


"""


# 3--嵌套函数举例: 工厂函数
def maker(N):
    def action(X):
        return X ** N
    return action


f = maker(2)    # pass 2 to N, N为封闭函数局部变量
f(3)            # 9, pass 3 to X, X为局部变量



# 4--嵌套函数举例: lambda实例
def maker(N):
    action = (lambda X: X ** N)     # 括号加不加无所谓
    return action

f = maker(2)    # pass 2 to N
f(3)        # pass 3 to X

# 5--nonlocal和global语句的区别
# nonlocal应用于一个嵌套的函数的作用域中的一个名称, 例如:
start = 100
def tester1(start):
    def nested(label):
        nonlocal start      # 指定start为tester函数内的local变量, 而不是global变量start
        print(label, start)
        start += 3
    return nested

def tester2(start):
    def nested(label):
        global start      # 指定start为global变量start
        print(label, start)
        start += 3
    return nested




# 6--函数参数, 不可变参数通过"值"传递, 可变参数通过"引用"传递
# 理解值传递, 引用传递
# 理解位置匹配, 关键字匹配

# def f(a, b, c): print(a, b, c)
# f(1, 2, 3)      # 参数位置匹配
# f(1, c=3, b=2)  # 参数关键字匹配
# def f(a, b=1, c=2): print(a, b, c)
# f(1)        # 默认参数匹配
# f(1, 2)     # 默认参数匹配
# f(a=1, c=3) # 关键字参数和默认参数的混合
# Keyword-Only参数: 出现在*args之后, 必须用关键字进行匹配
# def keyOnly(a, *b, c):print('')     # c就为keyword-only匹配, 必须使用关键字c=value匹配
# def keyOnly(a, *, c):print('')     # c就为keyword-only匹配, 必须使用关键字c=value匹配
# def keyOnly(a, *, b, c):print('')     # b, c就为keyword-only匹配, 必须使用关键字匹配
# def keyOnly(a, *, b=1):print('')     # b有默认值, 或者省略, 或者使用关键字参数b=value匹配




# 7--可变参数匹配: *和**
# def f(*args): print(args)    # 在元组中手机不匹配的位置参数
# f(1, 2, 3)    # 输出(1, 2, 3)
# def f(**args): print(args)    # 在字典中收集不匹配的关键字参数
# f(a=1, b=2)   # 输出{"a":1, "b":2}
# def f(a, *b, **c): print(a, b, c)   # 两者混合使用
# f(1, 2, 3, x=4, y=5)  # 输出1, (2, 3), {"x":4, "y":5}



# 8--函数调用时的参数解包: *和** 分别解包元组和字典
# def func(a,b,c): print(a, b, c)
# func(1, *(2, 3))   <==>   func(1, 2, 3)
# func(1, **{"c":3, "b": 2})  <==> func(1, b=2, c=3)
# func(1, *(2, 3), **{"c":3, "b":2}) <==> func(1, 2, 3, b=2, c=3)


# 9--函数属性: (自己定义的)函数可以添加属性
# def func(): pass
# func.count = 1      # 自定义函数添加属性
# print.count = 1     # Error, 内置函数不可以添加属性


# 10--函数注解: 编写在def头部行, 主要用于说明参数范围, 参数类型, 返回值类型等
# def func(a:'spam', b:(1, 10), c:float) -> int:
#     print(a, b, c)
# print(func.__annotations__)  # {'a': 'spam', 'b': (1, 10), 'c': <class 'float'>, 'return': <class 'int'>}
# 编写函数注解的同时, 还是可以使用函数默认值, 并且注解的位置位于=号的前面
# def func(a:str='a', b:(1,10)=2, c:float=3) -> int:
#     print(a, b, c)
# func()




# 11--匿名函数: lambda
# f = lambda x ,y ,z: x + y + z   # 普通的匿名函数, 使用方法f(1, 2, 3)
# f = lambda x = 1, y = 1: x + y      # 带默认参数的匿名函数
# def action(x):  # 嵌套的匿名函数
#     return (lambda y: y+x)

# f = action(250)
# r = f(10)
# print(r)

# f = lambda :a if xxx() else b   # 无参数的lambda函数, 使用方法: f()



# 12--lambda参数与map, filter, reduce函数的结合
list(map(lambda x: x+1, [1, 2, 3]))     # [2, 3, 4]
list(filter(lambda x: x>0, range(-4,5)))
import functools
functools.reduce(lambda x, y: x + y, [1, 2, 3])
functools.reduce(lambda x, y: x * y, [2, 3, 4])


# 13--生成器函数: yield VS return
# def gensqure(N):
#     for i in range(N):
#         yield i ** 2        # 状态挂起, 可以恢复到此时状态
# for i in gensqure(5):
#     print(i, end=' ')

# x = gensqure(2)     # x是一个生成器对象
# next(x)     # 等同于x.__next__()   # 返回0
# next(x)     # 等同于x.__next__()   # 返回1
# next(x)     # 等同于x.__next__()   # 抛出异常StopIteration



# 14--生成器表达式: 小括号进行列表解析
# G = (x**2 for x in range(3))    # 使用小括号可以创建所需结果的生成器generator object
# next(G), next(G), next(G)       # 和上述中的生成器函数的返回值一致
# (1) 生成器(生成器函数/生成器表达式)是单个迭代对象
# G = (x**2 for x in range(4))
# print(G)
# I1= iter(G)     # 这里实际上iter(G) = G, 可查看其id
# next(I1)
# next(G)
# next(I1)
# (2) 生成器不保留迭代后的结果
# gen = (i for i in range(4))
# print(2 in gen)     # 返回True
# print(3 in gen)     # 返回True
# print(1 in gen)     # 返回False, 其实检测2的时候, 1就已经不再生成器中了, 即1已经被迭代过了, 同理: 2, 3也不在了




# 15--本地变量是静态检测的
X = 22
# def test():
#     print(X)    # 如果没有下一语句, 该语句合法, 打印全局变量X
    # X = 88      # 这一语句使得上一语句非法, 因为它使得X变成了本地变量, 上一句变成了打印一个未定义的本地变量(局部变量)
    # if False:   # 即使这样的语句, 也会把print语句视为非法语句, 因为python会无视if语句而仍然声明了局部变量X
    #     X = 88
def test():     # 改进
    global X    # 声明变量X为全局变量
    print(X)    # 打印全局变量X
    X = 88      # 改变全局变量X


# 16--函数的默认值是在函数定义的时候实例化的, 而不是在调用的时候
# def foo(numbers=[]):
#     numbers.append(9)
#     print(numbers)
# foo()   # first time, [9]
# foo()   # second time, [9, 9]
# foo()   # third time, [9, 9, 9]
# foo([1, 2])  # [1, 2, 9]

# 改进:
# def foo(numbers=None):
#     if numbers is None:
#         numbers = []
#     print(numbers)

# 另外一个例子: 参数的默认值为不可变的:
# def foo(count=0):   # 这里的0是数字, 是不可变的
#     count += 1
#     print(count)
# foo()   # 输出是1
# foo()   # 还是输出1
# foo(3)   # 输出4
# foo()   # 还是输出1
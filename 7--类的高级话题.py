# 七. 类的高级话题

# 1--多重继承: "混合类", 搜索方式: 从下到上, 从左到右, 广度优先
# class A(B, C):
#     pass

# 2--类的基础和子类的初始化
# 1. 子类定义了__init__方法时, 若未显示调用基类__init__方法, python不会帮你调用
# 2. 子类未定义__init__方法时, python会自动帮你调用首个基类的__int__方法, 注意是首个
# 3. 子类显示调用基类的初始化函数:



class FooParent(object):
    def __init__(self, a):
        self.parent = "I 'm the Parent."
        print("Parent: a=" + str(a))

    def bar(self, message):
        print(message + ' from Parent')

class FooChild(FooParent):
    def __init__(self, a):
        FooParent.__init__(self, a)
        print('Child:a=' + str(a))

    def bar(self, message):
        FooParent.bar(self, message)
        print(message + ' from Child')

# fooChild = FooChild(10)
# fooChild.bar('HelloWorld')

# 实例方法 / 静态方法 / 类方法
# class Methods(object):
#     def imeth(self, x): print(self, x)  # 实例方法, 传入的是实例和数据, 操作的是实例的属性; 有self默认是实例方法.

    # def smeth(x): print(x)  # 静态方法: 只传入数据, 不传入实例, 操作的是类的属性而不是实例的属性. 没有self, 默认是静态方法

    # def cmeth(cls, x): print(cls, x)    # 类方法, 传入的是类对象和数据.  不定义成类方法的话, 它还是实例方法

    # smeth = staticmethod(smeth)     # 调用内置函数, 也可以使用@staticmethod

    # cmeth = classmethod(cmeth)      # 调用内置函数, 也可以使用@classmethod

# obj = Methods()
# obj.imeth(1)    # 实例方法调用
# Methods.imeth(obj, 2)   # 实例方法调用
# Methods.smeth(3)    # 静态方法调用
# obj.smeth(4)  # 这里可使用实例进行调用
# Methods.cmeth(5)    # 类方法调用
# obj.cmeth(6)



# 3--函数装饰器: 是它后面的函数的运行时的声明, 由@符号以及后面紧跟的"元函数"(metafunction)组成
# @staticmethod
# def smeth(x): print(x)
# 等同于:
# def smeth(x): print(x)
# smeth = staticmethod(smeth)
# 同理:
# @classmethod
# def cmeth(cls, x): print(x)
# 等同于
# def cmeth(cls, x): print(x)
# cmeth = staticmethod(cmeth)





# 4--类修饰器: 是它后边的类的运行时的声明, 由@符号以及后面紧跟的"元函数"(metafunction)组成
def decorator(aClass):
    # print("doSomething")
    pass
# @decorator
# class C(object): pass
# 等同于:
# class C(object): pass
# C = decorator(C)


# 5--限制class属性:__slots__属性
class Student(object):
    __slots__ = ('name', 'age')     # 限制Student及其实例只能拥有name和age属性
    # __slots__属性只对当前类起作用, 对其子类不起作用
    # __slots__属性能够节省内存
    # __slots__属性可以为列表list, 或者元组tuple



# 6--类属性的高级话题: @property
# 假设定义了一个类: C, 该类必须继承自object类, 有一私有变量__x
class C(object):
    def __init__(self):
        self.__x = None

# 第一种使用属性的方法
    def getx(self):
        # print("getx被调用")
        return self.__x

    def setx(self, value):
        # print("setx被调用")
        self.__x = value

    def delx(self):
        # print("delx被调用")
        del self.__x
    x = property(getx, setx, delx, '')
    # property函数原型为property(fget=None, fset=None, fdel=None, doc=None)
# 使用
c = C()
c.x = 100   # 自动调用setx方法
y = c.x     # 自动调用getx方法
del c.x     # 自动调用delx方法
# print(c.__x)
# print(c._x)

# 第二种使用属性的方法
class C(object):
    def __init__(self):
        self.__x = None
    @property
    def x(self):
        # print("获取")
        return self.__x

    @x.setter
    def x(self, value):
        # print("引用")
        self.__x = value

    @x.deleter
    def x(self):
        # print("删除")
        del self.__x
# 使用
c = C()
c.x = 100    # 自动调用setter方法
y = c.x     # 自动调用x方法
del c.x     # 自动调用deleter方法




# 7--定制类: 重写类的方法
# (1)__str__方法, __repr__方法: 定制类的输出字符串
# (2)__iter__方法, __next__方法: 定制类的可迭代性
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1   # 初始化两个计数器a，b
    def __iter__(self):
        return self     # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration
        return self.a
# for n in Fib():
    # print(n)    # 使用

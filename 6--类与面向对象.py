# 六. 类与面向对象

# 1--最普通的类
class C1(object):
    spam = 42   # 数据属性
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("good bye", self.name)

# I1 = C1('Bob')


# 2--Python的类没有基于参数的函数重载
# class FirstClass(object):
    # def test(self, string): # 被后面覆盖掉了
    #     print(string)
    #
    # def test(self):     # 此时类中只有一个test函数, 即后者test(self), 它覆盖掉前者带参数的test函数
    #     print("hello world")
# 3--子类扩展超类: 尽量调用超类的方法
# class Manager(Person):
#     def giveRaise(self, percent, bonus = .10):
        # self.pay = int(self.pay*(1+percent + bonus))    # 不好的方式, 复制粘贴超类代码
    # Person.giveRaise(self, percent+bonus)   # 好的方式, 尽量调用超类方法; 超类, 就是父类, 定义类括号里的内容

# 3--类的命名空间
# class Member(object):
#     count = 0
#     def init(self):
#         Member.count += 1
# print(Member.count)
# t1 = Member()
# t1.init()
# print(t1.count)
# print(Member.count)
# t2 = Member()
# t2.init()
# print(t2.count)
# print(Member.count)


# 4--类内省工具
class Person: pass
bob = Person()
# bob.__class__   # <class '__main__.Person'>
# bob.__class__.__name__  # Person
# bob.__dict__


# 5--返回1中, 数据类型spam是数据类 ,而不是对象



# 6--类方法调用的两种方式
# instance.method(arg...) # 实例.方法(参数)
# class.method(instance, arg...)    # 类名.方法(实例, 参数)
# class A():
#     def test(self, *args):
#         print("A-test", args)

# a = A()
# a.test(1234)
# A.test(a, 1234, 5678)




# 7--抽象超类的实现方法:
# 超类:super()
# 抽象类: 一般而言, 抽象类是不能实例化的类, 其职责是定义子类应实现的一组抽象方法
# 抽象超类: 类的部分行为由子类来提供. 如果预期的方法在子类中没有定义, 那么会抛出没有定义变量名的异常;

# (1)某个函数中调用未定义的函数, 子类中定义该函数
# def delegate(self):
#     self.action()     # 本类中不定义action函数, 所有使用delegate函数时就会出错

# (2)定义action函数, 但是返回异常
# def action(self):
#     raise NotImplementedError('action must be defined')

# (3)上述的两种方法还都可以定义实例对象, 实际上可以利用@装饰器语法生成不能定义的抽象超类



# from abc import ABCMeta, abstractclassmethod
# class Super(metaclass=ABCMeta):
#     @abstractclassmethod    # 这个类不能再被定义了
#     def action(self):
#         pass
# x = Super() # TypeError: Can't instantiate abstract class Super with abstract methods action



# 8--OOP: 面向对象编程: object-oriented programming
# (一)OOP和继承: 'is-a'的关系
class B:pass
class A(B): pass
a = A()
isinstance(a, B)  # 返回True    # A是B的子类, a也是B的一种
# type不会认为子类是一种父类类型, isinstance会认为子类是一种父类类型
# print(type(a) == A)     # True
# print(type(a) == B)     # False
# print(type(a))
# print(a)
# (二)OOP和组合: "has-a"的关系
class A(object):
    def __init__(self,name):
        self.name = name

class B(object):
    def __init__(self,phone):
        self.phone = phone

class C(object):
    def __init__(self, name, phone):
        self.name = A(name)     # 组合
        self.phone = B(phone)   # 组合

# (三)OOP和委托: "包装"对象, 在python中委托通常是以"__getattr__"钩子方法实现的, 这个方法会拦截对不存在属性的读取
# 包装类(或者成为代理类)可以使用__getattr__把任意读取转发给被包装的对象
class wrapper(object):
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attrname):
        print('Trace', attrname)
        return getattr(self.wrapped, attrname)

    # 注: 这里使用getattr(X, N)内置函数以变量名字符串N从包装对象X中取出属性. 类似于X.__dict__[N]
x = wrapper([1, 2, 3])
# x.append(4) # 返回Trace: append" [1, 2, 3, 4]
# x = wrapper({'a':1, 'b':2})
# print(list(x.keys()))  # 返回 "Trace: keys" ['a', 'b']

# todo # https://zhuanlan.zhihu.com/p/40446047
# todo https://zhuanlan.zhihu.com/p/29747657

# 9--类的伪私有属性: 使用__attr
class C1(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return "self.name = %s" %self.__name

I = C1('tom')
# print(I)    # 返回 self.name = tom
# I.__name = 'jeey'    # 这里无法访问, __name为伪私有属性
I._C1__name = 'jeey'    # 这里可以修改成功, self.name = jeey


# 10--类方法是对象: 无绑定类方法对象 / 绑定实例方法对象
# class Spam(object):
#     def doit(self, message):
#         print(message)

    # 静态方法
    # def selfless(message):
    #     print(message)

# obj = Spam()
# x = obj.doit    # 类的绑定方法对象   实例+函数
# x('hello world')
# x = Spam.doit   # 类的无绑定方法对象   类名 + 函数
# x(obj, 'hello world')
# x = Spam.selfless   # 类的无绑定方法函数, 在3.0之前无效
# x('hello world')




# 11--获取对象信息: 属性和方法
class Myobject: pass
a = Myobject()
dir(a)
hasattr(a, 'x')     # 测试是否有x属性或方法, 即a.x是否已经存在
setattr(a, 'y', 19) # 设置属性或方法, 等同于a.y = 19
# 这里有个很骚的技巧, 就是setattr可以设置一个不能访问到的属性, 即只能用getattr获取
setattr(a, "can't touch", 100)  # 这里的属性名带有空格, 不能直接访问
# print(getattr(a, "can't touch"))    # 但是可以用getattr获取

class A(object):
    def __init__(self):
        self.__name = "Luke"
        self.name = "luke"
    def get_name(self):
        return self.__name
a = A()
# print(a.get_name())
# print(hasattr(a,'get_name'))
# print(hasattr(a,'__name')
# print(getattr(a, '__name'))     # 报错
# print(setattr(a, '__name', "zhangsan"))
# print(getattr(a, '__name'))     # 设置之后获取到的是zhangsan



# 12--为类动态绑定属性或方法: MethodType方法
# 一般创建了一个class的实例后, 可以给该实例绑定任何属性和方法, 这就是动态语言的灵活性
# class Student(object):
#     pass

# s = Student()
# s.name = 'Michael'  # 动态给实例绑定一个属性
# def set_age(self, age):     # 定义函数作为实例方法
#     self.age = age
# from types import MethodType
# s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法, 类和其它实例不受此印象
# s.set_age(25)   # 调用实例方法
# print(s.age)
# Student.set_age = MethodType(set_age, Student)  # 为类绑定一个方法, 类的所有实例都拥有该方法
# w = Student()
# w.set_age(10)
# print(w.age)



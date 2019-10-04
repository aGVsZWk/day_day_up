# -*- coding: utf-8 -*-
# author: Luke


"""
# abc -- 抽象基类
该模块提供了用于在Python中定义抽象基类（ABC）的数据结构
collections模块有一些从ABCs派生的具体类。collections.abc子模块具有一些可用于测试类或实例是否提供特定接口的ABC，例如，它是哈希表还是映射。
"""



# register(subclass)
from abc import ABCMeta, abstractmethod
class MyABC(metaclass=ABCMeta):
    """将subclass注册为此ABC的虚拟子类。"""
    pass

MyABC.register(tuple)
assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)


# ABCMeta
# 定义类的时候指定metaclass，将方法用@abc.abstractmethod装饰，该方法不能被调用，只能用作被派生(继承，被别人)
class Factory(metaclass=ABCMeta):
    @abstractmethod
    def create_course(self):
        pass


f = Factory()
f.create_course()


# 案例见设计模式1 创建性  2.2 工厂方法设计模式

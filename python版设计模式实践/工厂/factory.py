import abc


class ABstractFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def make_object(self):
        return


class ConcreteFactory(ABstractFactory):
    # concrete: 缺失的，具体的；有形的，实在的
    def make_object(self):
        # do something
        return ConcreteClass()

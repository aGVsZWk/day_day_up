from typing import List, Iterator
from exceptions import ArgsException

class ArgumentMarshaler(object):
    def set(self, currentArgument: List[str]) -> None:
        pass


class BooleanArgumentMarshaler(ArgumentMarshaler):
    booleanValue = False

    def set(self, currentArgument: List[str]) -> None:
        self.booleanValue = True

    def getValue(self, am: BooleanArgumentMarshaler) -> bool:
        if am is not None and isinstance(am, ArgumentMarshaler):
            return am.booleanValue
        else:
            return False


class StringArgumentMarshaler(ArgumentMarshaler):
    stringValue = ''

    def set(self, currentArgument: Iterator[str]) -> None:
        try:
            stringValue = next(currentArgument)
        except:
            raise ArgsException('MISSING_STRING')

    def getValue(self, am: ArgumentMarshaler) -> None:
        if am is not None and isinstance(am, StringArgumentMarshaler):
            return am.stringValue
        else:
            return ''





a = [1, 2, 3]  # list is Iterator and Iterable
next(iter(a))  # next recive an Iterator
b = {1: 'a', 2: 'b', 3: 'c'} # Dict is Iterable, not Iterator
t = iter(b)    # iter return an Iterator
next(t)


class A(object):
    def __init__(self, xxx):
        self.xxx = xxx

    def a(self, a):
        if isinstance(a, A):
            return a.xxx

a = A('qwe')
aa = A(123)
aa.a(a)    # qwe

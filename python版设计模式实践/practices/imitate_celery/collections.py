# -*- coding: utf-8 -*-
import sys
from collections import OrderedDict as _OrderedDict
from collections import deque
from heapq import heapify, heappop, heappush
from itertools import chain, count

# try:
from collections import Callable, Mapping, MutableMapping, MutableSet
from collections import Sequence



def items(d):
    """Get dict items iterator."""
    return d.items()

def keys(d):
    """Get dict keys iterator."""
    return d.keys()

def values(d):
    """Get dict values iterator."""
    return d.values()

def nextfun(it):
    """Get iterator next method."""
    return it.__next__

def reraise(tp, value, tb=None):
    """Reraise exception."""
    if value.__traceback__ is not tb:
        raise value.with_traceback(tb)
    raise value



class OrderedDict(_OrderedDict):
    """Dict where insertion order matters."""
    def _LRUkey(self):
        return next(iter(keys(self)))


class AttributeDictMixin(object):
    """Minin for Mapping iterface that adds attribute access.
    `d.key -> d[key]`
    """

    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError:
            raise AttributeError('{0!r} object has no attribute {1!r}'.format(
                type(self).__name__, k ))

    def __setattr__(self, key, value):
        """`d[key] = value -> d.key = value`"""
        self[key] = value


class AttributeDict(dict, AttributeDictMixin):
    """Dict subclass with attribute access"""


class DictAttribute(object):
    """Dict interface to attributes.
    `obj[key] -> obj.k`
    `obj[k] = val -> obj.k = val`
    """
    obj = None

    def __init__(self, obj):
        object.__setattr__(self, 'obj', obj)

    def __getattr__(self, key):
        print("aaa")
        print(self.obj)
        return getattr(self.obj, key)

    def __setattr__(self, key, value):
        print("bbb")
        print(self.obj)
        return setattr(self.obj, key, value)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def setdefault(self, key, default=None):
        if key not in self:
            self[key] = default

    def __getitem__(self, key):
        try:
            return getattr(self.obj, key)
        except AttributeError:
            raise KeyError(key)

    def __setitem__(self, key, value):
        setattr(self.obj, key, value)

    def __contains__(self, key):
        return hasattr(self.obj, key)

    def _iterate_keys(self):
        return iter(dir(self.obj))

    iterkeys = _iterate_keys

    def __iter__(self):
        return self._iterate_keys()

    def _iterate_items(self):
        for key in self._iterate_keys():
            yield key, getattr(self.obj, key)
    iteritems = _iterate_items

    def _iterate_values(self):
        for key in self._iterate_keys():
            yield getattr(self.obj, key)
    itervalues = _iterate_values
# "{0!r:20}".format("Hello")



MutableMapping.register(DictAttribute)  # noqa: E305



class ChainMap(MutableMapping):
    """key lookup on a sequence of maps"""
    key_t = None
    changes = None
    defaults = None
    maps = None
    _observers = []

    def __init__(self, *maps, **kwargs):
        maps = list(maps or [{}])
        self.__dict__.update(
            key_t=kwargs.get('key_t'),
            maps=maps,
            changes=maps[0],
            defaults=maps[1:]
        )






for i in count(3,2):
    if i > 20:break
    print(i)

for i in chain('ABC', 'DEF'):
    print(i)

# keys(chain('ABC', 'DEF'))

a = {"w":2}
a.keys()
a = OrderedDict({"a": 10, "b":20})
a.move_to_end('a')
a

c = DictAttribute(a)
c.b = 3
w = c.b
w

w = [{}]
w[0]
w[1:]

a = {"a":10}
a = dict(a)
a.a

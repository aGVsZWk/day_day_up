# -*- coding: utf-8 -*-
# @Author: helei
# @Date:   2021-01-29
# @Email:  v_heleihe@tencent.com
# @Filename: aa.py
# @Last modified by:   helei
# @Last modified time: 2021-01-29
[[1,2,3,4,5],[7,8,9]] => [1,2,3,4,5,6,7,8,9]


a =  [[1,2,3,4,5],[7,8,9]]


def tranList(inputList):
    ret = []
    for i in inputList:
        ret += i
    return ret


tranList(a)

from operator import add
list(reduce(add, a))


class SingleInstance(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = True
            return super().__new__(cls, *args, **kwargs)



inputList = [1,2,3,4,4,4,4,5,6,7,8]

index(4, inputList)


inputList.index(4)

def find_elem(elem=4):
    ret = -1
    i, j = 0, len(inputList) - 1
    mid = (i + j) // 2
    while i != j:
        if inputList[j] >= elem:
            j = (i + j) // 2 + 1
        if inputList[i] < elem:
            i = (i + j) // 2 - 1

    if elem != inputList[i]:
        return -1
    else:
        return ret

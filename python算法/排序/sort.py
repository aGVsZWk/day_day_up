# 插入排序
def insertSort(target):
    for j in range(1, len(target)):
        key = target[j]
        i = j - 1
        while i >= 0 and target[i] > key:
            target[i+1] = target[i]
            i -= 1
        target[i+1] = key
    return target


# 选择排序
def selectSort(target):
    for i in range(0, len(target) - 1):
        t = i
        for j in range(i+1, len(target)):
            if target[j] < target[t]:
                t = j
        target[i], target[t] = target[t], target[i]

    return target


# 冒泡排序
def bulletSort(target):
    for i in range(0, len(target)):
        for j in range(0, len(target)-1-i):
            if target[j] > target[j+1]:
                target[j+1], target[j] = target[j], target[j+1]
    return target


# 归并排序
def mergeSort(target, p, r):
    if p < r:
        q = (p + r) // 2
        # 分解
        mergeSort(target, p, q)
        mergeSort(target, q+1, r)
        # 解决+合并
        merge(target, p, q, r)
    return target

def merge(target, p, q, r):
    # 创建新数组
    import copy
    l1 = copy.copy(target[p:q+1])
    l2 = copy.copy(target[q+1:r+1])
    # l1 = []
    # l2 = []
    # for i in range(p, q+1):
    #     l1.append(target[i])
    # for i in range(q+1, r+1):
    #     l2.append(target[i])
    # 新数组增加无穷大哨兵
    l1.append(float("inf"))
    l2.append(float("inf"))
    # 分发元素(合并)
    i = 0
    j = 0
    for k in range(p, r+1):
        if l1[i] <= l2[j]:
            target[k] = l1[i]
            i += 1
        else:
            target[k] = l2[j]
            j += 1

# 快速排序
def quickSort(target, p, r):
    if p < r:
        q = partition(target, p, r)
        quickSort(target, p, q-1)
        quickSort(target, q+1, r)
    return target

def partition(target, p, r):
    # 每次选取最右侧元素作为主元，循环结束之后，将主元的正确位置返回
    key = target[r]
    i = p
    # i 是所有大于主元的元素，扫描到比主元小的元素，就换一次！把所有 i 换成小于的，前面的元素就会比后面的小！完事！！！
    for j in range(p, r):
        if target[j] <= key:
            target[i], target[j] = target[j], target[i]
            i += 1
    target[i], target[r] = target[r], target[i]
    return i

def shellSort(target):
    step = len(target) // 2
    while step > 0:
        for j in range(step, len(target)):
            key = target[j]
            i = j - step
            while i >= 0 and target[i] > key:
                target[i+step] = target[i]
                i -= step
            target[i+step] = key
        step //= 2
    return target

import unittest

class TestSort(unittest.TestCase):
    def setUp(self):
        self.target = [1, 5, 6, 4, 2, 3, 6]
        self.result = [1, 2, 3, 4, 5, 6, 6]

    def test_insert_sort(self):
        self.assertEqual(self.result, insertSort(self.target))

    def test_select_sort(self):
        self.assertEqual(self.result, selectSort(self.target))

    def test_bullet_sort(self):
        self.assertEqual(self.result, bulletSort(self.target))

    def test_merge_sort(self):
        self.assertEqual(self.result, mergeSort(self.target, 0, len(self.target)-1))

    def test_quick_sort(self):
        self.assertEqual(self.result, quickSort(self.target, 0, len(self.target)-1))

    def test_shell_sort(self):
        import random
        self.case = [random.randint(-10000, 10000) for i in range(1000)]
        self.assertEqual(sorted(self.case), shellSort(self.case))

if __name__ == '__main__':
    unittest.main()

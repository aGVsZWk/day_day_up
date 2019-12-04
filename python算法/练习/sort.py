def bulletSort(target):
    for i in range(0, len(target)):
        for j in range(0, len(target)-1-i):
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]
    return target


def selectSort(target):
    for i in range(0, len(target)):
        min_ = target[i]
        for j in range(i+1, len(target)):
            if target[j] < min_:
                min_, target[j] = target[j], min_
        target[i] = min_
    return target


def insertSort(target):
    for i in range(1, len(target)):
        key = target[i]
        j = i - 1
        while j >= 0 and key < target[j]:
            target[j+1] = target[j]
            j -= 1
        target[j+1] = key   # 要加 1 ，注意跳出循环的时候
    return target


def mergeSort(target, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(target, p, q)
        mergeSort(target, q+1, r)
        merge(target, p, q, r)
    return target

def merge(target, p, q, r):
    import copy
    l1 = copy.copy(target[p:q+1])
    l2 = copy.copy(target[q+1:r+1])
    l1.append(float("inf"))
    l2.append(float("inf"))
    m = 0
    n = 0
    for i in range(p, r+1):  # ！！！注意范围
        if l1[m] <= l2[n]:      # ！！！ 注意比较内容
            target[i] = l1[m]
            m += 1
        else:
            target[i] = l2[n]
            n += 1


import unittest


class TestSort(unittest.TestCase):

    def setUp(self):
        self.target = [1, 5, 6, 4, 2, 3]
        self.result = [1, 2, 3, 4, 5, 6]

    def test_bullet_sort(self):
        ret = bulletSort(self.target)
        self.assertEqual(self.result, ret)

    def test_select_sort(self):
        ret = selectSort(self.target)
        self.assertEqual(self.result, ret)

    def test_insert_sort(self):
        ret = insertSort(self.target)
        self.assertEqual(self.result, ret)

    def test_merge_sort(self):
        ret = mergeSort(self.target, 0, len(self.target)-1)
        self.assertEqual(ret, self.result)

if __name__ == '__main__':
    unittest.main()

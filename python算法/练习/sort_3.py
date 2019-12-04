def mergeSort(target, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(target, p, q)
        mergeSort(target, q+1, r)
        merge(target, p, q, r)

def merge(target, p, q, r):
    import copy
    l1 = copy.copy(target[p:q+1])
    l2 = copy.copy(target[q+1:r+1])
    l1.append(float('inf'))
    l2.append(float('inf'))
    m, n = (0, 0)
    for i in range(p, r+1):
        if l1[m] <= l2[n]:
            target[i] = l1[m]
            m += 1
        else:
            target[i] = l2[n]
            n += 1

def insertSort(target):
    for i in range(1, len(target)):
        key = target[i]
        j = i - 1
        while j >= 0 and target[j] > key:
            target[j+1] = target[j]
            j -= 1
        target[j+1] = key

import unittest


def selectSort(target):
    for i in range(0, len(target)):
        min_ = target[i]
        for j in range(i+1, len(target)):
            if min_ > target[j]:
                min_, target[j] = target[j], min_
        target[i] = min_


def bulletSort(target):
    for i in range(0, len(target)):
        for j in range(0, len(target)-i-1):
            if target[j] >  target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]

class TestSort(unittest.TestCase):

    def setUp(self):
        self.target = [1, 5, 6, 4, 2, 3]
        self.result = [1, 2, 3, 4, 5, 6]

    def test_bullet_sort(self):
        bulletSort(self.target)
        self.assertEqual(self.result, self.result)
    #
    def test_select_sort(self):
        selectSort(self.target)
        self.assertEqual(self.result, self.result)
    #
    def test_insert_sort(self):
        insertSort(self.target)
        self.assertEqual(self.result, self.target)

    def test_merge_sort(self):
        mergeSort(self.target, 0, len(self.target)-1)
        self.assertEqual(self.result, self.target)

if __name__ == '__main__':
    unittest.main()

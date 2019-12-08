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
    for i in range(p, q+1):
        if target[m] < target[n]:
            target[i] = target[m]
            m += 1
        else:
            target[i] = target[n]
            n += 1


def insertSort(target):
    for i in range(1, len(target)):
        key = target[i]
        j = i - 1
        while key < target[j]:
            target[j+1] = target[j]
            j -= 1
        target[j+1] = key


def selectSort(target):
    for i in range(0, len(target)):
        min_ = target[i]
        for j in range(i+1, len(target)):
            if min_ > target[j]:
                min_, target[j] = target[j], min_
        target[i] = min_


def bulletSort(target):
    for i in range(0, len(target)):
        for j in range(0, len(target) - 1 - i):
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]

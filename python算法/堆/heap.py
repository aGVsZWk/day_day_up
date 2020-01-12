class MaxHeap(object):

    def __init__(self, maxSize=None):
        self.maxSize = maxSize
        self._elements = [None] * maxSize
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxSize:
            raise Exception("full")
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count - 1)

    def _siftup(self, ndx):
        if ndx > 0:
            parent = (ndx - 1) // 2
            if self._elements[ndx] > self._elements[parent]:
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
            self._siftup(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception("empty")
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self, ndx):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        largest = ndx
        # 左右都有
        if right < self._count:
            if self._elements[left] > self._elements[right] and self._elements[left] > self._elements[largest]:
                largest = left
            elif self._elements[right] >= self._elements[left] and self._elements[right] >= self._elements[largest]:
                largest = right
        # 只有一个
        elif left == self._count:
            if self._elements[left] > self._elements[largest]:
                largest = left
        # 没有子孩子
        else:
            largest = ndx
        if largest != ndx:
            self._elements[ndx], self._elements[largest] = self._elements[largest], self._elements[ndx]
            self._siftdown(largest)

def test_maxheap():
    import random
    h = MaxHeap(100000000)
    for i in range(10000):
        h.add(random.randint(0, 10000))
    for i in reversed(range(10000)):
        print(h.extract())




if __name__ == '__main__':
    test_maxheap()

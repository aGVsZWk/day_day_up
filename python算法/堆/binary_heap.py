class BinHeap(object):
    def __init__(self):
        self.heapList = [0]     # 下表为 0 的项无用
        self.currentSize = 0

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        # 上浮
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i == i // 2

    def delMin(self):
        retval = self.heapList[1]   # 移走堆顶
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.perDown(1)   # 新顶下沉
        return retval

    def perDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self, i):
        # 唯一子节点
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            # 较小子节点
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + len(alist)
        print(len(self.heapList), i)
        while i > 0:
            print(self.heapList, i)
            self.perDown(i)
            i -= 1
        print(self.heapList, i)

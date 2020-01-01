class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1       # 增加到最后位置
        self.percUp(self.currentSize)   # 进行上浮操作，和父节点进行比较

    def percUp(self, i):
        while i // 2 > 0:       # i // 2 表示它的父节点，二叉树的性质
            if self.heapList[i] > self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i //= 2

    def delMin(self):
        # 用右节点代替堆顶节点，还要写下沉

        # 移出堆顶
        retVal = self.heapList[1]
        # 把最后一个搬到堆顶来
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retVal

    def percDown(self. i):
        # 将父节点与左右子孩子中较小的进行比较
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self, i):
        # 返回子孩子中较小的
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def buildHeap(self, alist):
        # 将列表转换成堆 --- > 从中间开始不断下沉
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i -= 1

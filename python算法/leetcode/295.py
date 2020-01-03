class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.big_queue = []
        self.small_queue = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.big_queue) == 0:
            self.big_queue.append(num)
            return

        if len(self.big_queue) == len(self.small_queue):
            if num < max(self.big_queue):
                self.big_queue.append(num)
            else:
                self.small_queue.append(num)
        elif len(self.big_queue) > len(self.small_queue):
            if num > max(self.big_queue):
                self.small_queue.append(num)
            else:
                t = max(self.big_queue)
                self.big_queue.remove(t)
                self.small_queue.append(t)
                self.big_queue.append(num)
        else:
            if num < min(self.small_queue):
                self.big_queue.append(num)
            else:
                t = min(self.small_queue)
                self.small_queue.remove(t)
                self.big_queue.append(t)
                self.small_queue.append(t)


    def findMedian(self):
        """
        :rtype: float
        """
        print(self.big_queue, self.small_queue)
        if len(self.big_queue) > len(self.small_queue):
            return max(self.big_queue)
        elif len(self.big_queue) < len(self.small_queue):
            return min(self.small_queue)
        else:
            return (max(self.big_queue) + min(self.small_queue)) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(1)
    print(obj.findMedian())
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())
    obj.addNum(4)
    print(obj.findMedian())
    obj.addNum(5)
    print(obj.findMedian())
    obj.addNum(6)
    print(obj.findMedian())
    obj.addNum(7)
    print(obj.findMedian())
    obj.addNum(8)
    print(obj.findMedian())

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.helper = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        while self.queue:
            t = self.queue[0]
            self.queue.remove(t)
            self.helper.append(t)
        self.queue.append(x)
        while self.helper:
            t = self.helper[0]
            self.helper.remove(t)
            self.queue.append(t)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        t = self.queue[0]
        self.queue.remove(t)
        return t

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return True if not self.queue else False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

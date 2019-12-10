class Stack(object):
    def __init__(self):
        self._stack = []

    def push(self, data):
        self._stack.append(data)

    def pop(self):
        if self._stack:
            return self._stack.pop()
        else:
            print("error: stack is empty")

    def isEmpty(self):
        return not bool(self._stack)

    def top(self):
        return self._stack[-1]

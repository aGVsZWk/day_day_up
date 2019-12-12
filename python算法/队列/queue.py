class Queue(object):
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        return self.queue.insert(0, data)

    def dequeue(self, data):
        return self.queue.append(data)

    def size(slef):
        return len(self.queue)

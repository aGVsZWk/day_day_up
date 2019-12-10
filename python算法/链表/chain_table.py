class Node(object):
    def __init__(self, data, pnext=None):
        self.data = data
        self._next = pnext

class ChainTable(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return (self.length == 0)

    def append(self, dataOrNode):
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)
        if not self.head:
            self.head = item
            self.length += 1
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

    def delete(self, index):
        if self.isEmpty():
            print("this chain table is empty")
            return
        if index < 0 or index > self.length:
            print("error: out of index")
            return
        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return
        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1
        if j == index:
            prev._next = node._next
            self.length -= 1

    def insert(self, index, dataOrNode):
        if self.isEmpty():
            print("this chain table is empty")
            return
        if index < 0 or index >= self.length:
            print("error: out of index")
            return

        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)
        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return
        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1
        if j == index:
            item._next = node
            prev._next = item
            self.length += 1

    def update(self, index, data):
        if self.isEmpty() or index < 0 or index >= self.length:
            print("error: out of index")
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1
        if j == index:
            node.data = data

    def getItem(self, index):
        if self.isEmpty() or index < 0 or index >= self.length:
            print("error: out of index")
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1
        return node.data

    def getIndex(self, data):
        if self.isEmpty():
            print("this chain table is empty")
            return
        j = 0
        node = node._next
        while node:
            if node.data == data:
                return j
            node = node._next
            j += 1
        if j == self.length:
            print("%s not found" % str(data))
            return

    def clear(self):
        self.head = None
        self.length = 0

    def __getitem__(self, index):
        if self.isEmpty() or index < 0 or index >= self.length:
            print("error: out of index")
            return
        return self.getItem(index)

    def __setitem__(self, index, data):
        if self.isEmpty() or index < 0 or index >= self.length:
            print("error: out of index")
            return
        self.update(index, data)

    def __len__(self):
        return self.length


import unittest

class TestChainTable(unittest.TestCase):

    def setUp(self):
        self.chain_table = ChainTable()

    def test_append(self):
        for i in range(0, 50):
            self.chain_table.append(i)
        for i in range(50, 100):
            self.chain_table.append(Node(i))
        for i in range(0, 100):
            self.assertEqual(i, self.chain_table.getItem(i))
            self.assertEqual(i, self.chain_table[i])

    def test_insert(self):
        self.test_append()
        self.chain_table.insert(0, 10000)
        self.assertEqual(10000, self.chain_table[0])
        self.chain_table.insert(0, Node(100000))
        self.assertEqual(100000, self.chain_table[0])
        import random
        index = random.randint(0, 102)
        value = random.randint(0, 10000)
        self.chain_table.insert(index, value)
        self.assertEqual(self.chain_table.length, 103)
        self.assertEqual(self.chain_table.getItem(index), value)

    def test_update(self):
        self.test_insert()
        self.chain_table.update(0, -1)
        self.assertEqual(self.chain_table[0], -1)
        import random
        index = random.randint(0, self.chain_table.length-1)
        value = random.randint(0, 10000)
        self.chain_table[index] = value
        self.assertEqual(self.chain_table.getItem(index), value)


    def test_delete(self):
        self.test_append()
        self.chain_table.delete(0)
        self.assertEqual(1, self.chain_table[0])
        import random
        index = random.randint(1, self.chain_table.length-1)
        value = self.chain_table[index+1]
        self.chain_table.delete(index)
        self.assertEqual(self.chain_table[index], value)

if __name__ == '__main__':
    unittest.main()

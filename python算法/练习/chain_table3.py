class Node(object):
    def __init__(self, data, pnext = None):
        self.data = data
        self._next = pnext


class ChainTable(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def append(self, dataOrNode):
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)
        if not self.head:
            self.head = item
            self.length += 1
            return
        node = self.head
        while node._next:
            node = node._next
        node._next = item
        self.length += 1


    def insert(self, index, dataOrNode):
        if index < 0 or index >= self.length:
            print("error: index out of range")
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)
        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return
        node = self.head
        prev = None
        j = 0
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1
        if j == index:
            item._next = node
            prev._next = item
            self.length += 1

    def delete(self, index):
        if index < 0 or index >= self.length:
            print("error: index out of range")
        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return
        node = self.head
        prev = None
        j = 0
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1
        if j == index:
            prev._next = node._next
            self.length -= 1

    def update(self, index, value):
        if index < 0 or index >= self.length:
            print("error: index out of range")
        node = self.head
        prev = None
        j = 0
        while node._next and j < index:
            node = node._next
            j += 1
        if j == index:
            node.data = value

###########################################################################
    def getItem(self, index):
        if index < 0 or index >= self.length or self.isEmpty():
            print("error: index out of range")
            return
        if index == 0:
            return self.head.data
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1
        if j == index:
            return node.data

    def getIndex(self, data):
        j = 0
        node = self.head
        while node._next and j < self.length:
            if node.data == data:
                return j
            j += 1
        print("error: not found %s" % data)

    def __setitem__(self, index, value):
        return self.update(index, value)

    def __getitem__(self, index):
        return self.getItem(index)


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
    #
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

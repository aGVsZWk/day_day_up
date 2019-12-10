from chain_table import ChainTable


class ChainTableDemos(ChainTable):
    def reverse(self):
        """反转链表"""
        if self.isEmpty():
            return
        if not self.head._next:
            return
        prev = None
        node = None
        next = self.head
        while next._next:
            prev = node
            node = next
            next = next._next
            node._next = prev
        next._next = node
        self.head = next


    def isLoop(self):
        """判断链表是否有环"""
        isLoopExist = False
        fast = self.head
        slow = self.head
        while fast and fast._next:
            slow = slow._next
            fast = fast._next._next
            if slow == fast:
                isLoopExist = True
                break
        return isLoopExist

    def removeNthFromEnd(self, n):
        """删除链表的倒数第n个节点"""
        if n <= 0:
            print("error: n is wrong")
        end = self.head
        before = self.head
        j = 0
        while j < n:
            end = end._next
            j += 1
        while end._next and j < self.length:
            end = end._next
            before = before._next
        before._next = before._next._next

    def getMiddleNode(self):
        """返回链表的中间节点(靠右)，也可使用统计长度的方法"""
        if self.isEmpty():
            print("error: chain table is empty")
        if not self.head._next:
            return self.head
        fast = self.head
        slow = self.head
        while fast and fast._next:
            fast = fast._next._next
            slow = slow._next
        return slow

def mergeTwoChainTables(l1, l2):
    """合并两个有序链表"""
    if not l1:
        return l2
    if not l2:
        return l1
    node1 = l1.head
    node2 = l2.head
    if node1.data < node2.data:
        node = node1
        node1 = node1._next
    else:
        node = node2
        node2 = node2._next
    chain_table = node
    while node1 and node2:
        if node1.data < node2.data:
            node._next = node1
            node = node._next
            node1 = node1._next
        else:
            node._next = node2
            node = node._next
            node2= node2._next
    if node1:
        node._next = node1
    if node2:
        node._next = node2
    return chain_table

import unittest
class ChainTableDemosTest(unittest.TestCase):
    def setUp(self):
        self.chain_table = ChainTableDemos()
        for i in range(100):
            self.chain_table.append(i)

    def test_reverse(self):
        end = self.chain_table.reverse()
        for i in range(0, 100):
            self.assertEqual(self.chain_table[i], 99-i)

    def test_middle_node(self):
        node = self.chain_table.getMiddleNode()
        self.assertEqual(node.data, 50)
        self.chain_table.append("a")
        node = self.chain_table.getMiddleNode()
        self.assertEqual(node.data, 50)
        self.chain_table.append("b")
        node = self.chain_table.getMiddleNode()
        self.assertEqual(node.data, 51)

    def test_has_loop(self):
        is_loop = self.chain_table.isLoop()
        self.assertEqual(is_loop, False)
        node = self.chain_table.head._next._next._next
        for i in range(30):
            node = node._next
        node._next = self.chain_table.head._next._next._next._next._next._next
        is_loop = self.chain_table.isLoop()
        self.assertEqual(is_loop, True)

    def test_remove_from_end(self):
        self.chain_table.removeNthFromEnd(1)
        self.assertEqual(self.chain_table[98], 98)
        self.chain_table.removeNthFromEnd(2)
        self.assertEqual(self.chain_table[97], 98)
        self.assertEqual(self.chain_table[96], 96)
        self.chain_table.removeNthFromEnd(3)
        self.assertEqual(self.chain_table[96], 98)
        self.assertEqual(self.chain_table[95], 96)
        self.assertEqual(self.chain_table[94], 94)

    def test_merge_chain_table(self):
        chain_table1 = ChainTable()
        chain_table2 = ChainTable()
        for i in range(0, 100):
            if i % 2 == 0:
                chain_table1.append(i)
            else:
                chain_table2.append(i)
        chain_table = mergeTwoChainTables(chain_table1, chain_table2)
        for i in range(0, 100):
            self.assertEqual(chain_table.data, i)
            chain_table = chain_table._next

if __name__ == '__main__':
    unittest.main()

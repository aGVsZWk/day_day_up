# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev, node, ne = None, None, head
        while ne:
            prev = node
            node = ne
            ne = ne.next
            node.next = prev
        return node

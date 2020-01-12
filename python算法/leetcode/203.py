# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        while head and head.val == val:
            head = head.next
        answer = prev = head
        while prev:
            head = head.next
            while head and head.val == val:
                head = head.next
            prev.next = head
            prev = prev.next
        return answer

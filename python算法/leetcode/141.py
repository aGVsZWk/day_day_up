# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = head
        fast = head.next
        # while fast:
        #     if slow != fast:
        #         slow = slow.next
        #         if fast.next:
        #             fast = fast.next.next
        #         else:
        #             fast = fast.next
        #     else:
        #         return True
        while fast and fast.next:
            if slow != fast:
                slow = slow.next
                fast = fast.next.next
            else:
                return True
        return False

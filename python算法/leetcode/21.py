# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 or l2):
            return
        target = ret = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                target.val = l1.val
                l1 = l1.next
            else:
                target.val = l2.val
                l2 = l2.next
            if l1 or l2:
                target.next = ListNode(0)
                target = target.next
            else:
                target.next = None
        if l1:
            target.val = l1.val
            target.next = l1.next
        if l2:
            target.val = l2.val
            target.next = l2.next
        return ret
        

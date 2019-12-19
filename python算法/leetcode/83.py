# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        ret = node = head
        next_ = head.next
        while next_:
            if node.val == next_.val:
                next_ = next_.next
            else:
                node.next = next_
                node = node.next
                next_ = next_.next
        if node:
            node.next = None
        return ret

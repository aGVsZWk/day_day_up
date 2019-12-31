# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p, q= headA, headB
        while p != q:
            # 将两个链表拼在一起，重合部分即为走过的 p + q 长度路径
            p = p.next if p else headB
            q = q.next if q else headA
        return p

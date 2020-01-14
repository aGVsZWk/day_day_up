# -*- coding: utf-8 -*-
# author: Luke
# 链表
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    # 反转操作
    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

# 双向链表
class DListNonde:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

    def reverse(self, head):
        curt = None
        while head:
            curt = head
            head = curt.next
            curt.next = curt.prev
            curt.prev = head
        return curt

# hu判断链表是否有环
class NodeCircle:
    def __init__(self, val):
        self.val = val
        self.next = None

    def has_circle(self, head):
        slow = head
        fast = head
        while (slow and fast):
            fast = fast.next
            slow = slow.next
            if fast:
                fast = fast.next
            if fast == slow:
                break
        if fast and slow and (fast == slow):
            return True
        else:
            return False





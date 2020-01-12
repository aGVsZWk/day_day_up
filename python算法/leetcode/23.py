# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        import heapq
        self._heap = []

        for list_ in lists:
            while list_:
                heapq.heappush(self._heap, list_.val)
                list_ = list_.next
        if not self._heap:
            return
        ret = a= ListNode(heapq.heappop(self._heap))
        while len(self._heap) != 0:
            t = ListNode(heapq.heappop(self._heap))
            ret.next = t
            ret = ret.next
        return a

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = nums[:k]

        for i in range(k, len(nums)):
            if nums[i] > min(l):
                l.remove(min(l))
                l.append(nums[i])
        return min(l)

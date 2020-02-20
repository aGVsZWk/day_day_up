class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            t = nums[:i] + nums[i+1:]
            if sorted(t) == t:
                return True
        return False


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == k:
            return sum(nums) / float(k)

        s = 0
        for i in range(0, len(nums) - k + 1):
            s = max(sum(nums[i: i+k]), s)
        return s / float(k)


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == k:
            return sum(nums) / float(k)

        s = float('-inf')
        t = sum(nums[:k])
        for i in range(0, len(nums) - k):
            s = max(s, t)
            t += nums[i+k] - nums[i]
        s = max(s, t)
        return s / float(k)

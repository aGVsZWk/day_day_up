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

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortNums = sorted(nums)
        if sortNums == nums:
            return 0
        for i in range(len(nums)):
            if nums[i] != sortNums[i]:
                break
        for j in range(len(nums)-1, -1, -1):
            if nums[j] != sortNums[j]:
                break
        return j - i + 1

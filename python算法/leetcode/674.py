class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        answer = 0
        increaseLength = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                increaseLength += 1
            else:
                answer = max(increaseLength, answer)
                increaseLength = 1
        answer = max(increaseLength, answer)
        return answer

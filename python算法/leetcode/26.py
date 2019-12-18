class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        pointer = 0
        for i in range(1, len(nums)):
            if nums[pointer] == nums[i]:
                continue
            else:
                nums[pointer+1] = nums[i]
                pointer += 1
        return pointer + 1

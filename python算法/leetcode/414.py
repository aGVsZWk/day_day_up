class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        first, second, third = nums[0], nums[1], nums[2]

        for num in nums:
            if num > first:
                first, second, third = num, first, second
            elif num < first and num > second:
                second, third = num, second
            elif num > third and num < second:
                third = num
        return third

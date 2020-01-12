class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        double_nums = nums + nums
        stack = []
        result = [-1] * len(nums)
        for index, num in enumerate(double_nums):
            while stack and num > nums[stack[-1]]:
                result[stack.pop()] = num
            if index < len(nums):
                stack.append(index)
        return result

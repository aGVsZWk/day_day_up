class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        max_position = nums[0]
        per_max_position = nums[0]
        times = 1

        for i in range(len(nums)):
            if i > max_position:
                times += 1
                max_position = per_max_position

            per_max_position = max(per_max_position, nums[i]+i)
        return times

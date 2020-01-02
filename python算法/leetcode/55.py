class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_position = 0
        for i, num in enumerate(nums):
            max_position = max(max_position, i+num)
            # 结束条件能优化
            while max_position < len(nums)-1 and i == max_position:
                return False
        return True



class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_position = 0
        for i, num in enumerate(nums):
            max_position = max(max_position, i+num)
            if max_position < len(nums) - 1:
                if i == max_position:
                    return False
            else:
                return True

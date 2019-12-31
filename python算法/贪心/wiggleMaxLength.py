# 摇摆序列 (leetcode 376)
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        self.state = 0
        self.max_length = 1

        for i in range(1, len(nums)):
            if self.state == 0:
                self.begin(i, nums)
            elif self.state == 1:
                self.up(i, nums)
            elif self.state == 2:
                self.down(i, nums)
        return self.max_length

    def begin(self, i, nums):
        if nums[i-1] > nums[i]:   # 下降
            self.state = 2
            self.max_length += 1
        elif nums[i-1] < nums[i]: # 上升
            self.state = 1
            self.max_length += 1

    def up(self, i, nums):
        if nums[i-1] > nums[i]:   # 下降
            self.state = 2
            self.max_length += 1

    def down(self, i, nums):
        if nums[i-1] < nums[i]:   # 上升
            self.state = 1
            self.max_length += 1

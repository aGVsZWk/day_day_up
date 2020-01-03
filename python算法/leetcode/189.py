class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # while k > 0:
        #     nums.insert(0, nums.pop())
        #     k -= 1

        k %= len(nums)
        if k == 0:
            return
        nums[:] = nums[-k:] + nums[:len(nums) - k]

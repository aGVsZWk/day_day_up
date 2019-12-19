# 暴破，超时了
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        for i in range(len(nums)):
            temp = nums[i]
            if temp > max_sum:
                max_sum = temp
            for j in range(i+1, len(nums)):
                temp += nums[j]
                if temp > max_sum:
                    max_sum = temp
        return max_sum

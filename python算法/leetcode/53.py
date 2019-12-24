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

# 有更简单的解法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        global_num, local_num = 0, 0
        for num in nums:
            local_num = max(0, num + local_num)
            global_num = max(local_num, global_num)
        return global_num
        

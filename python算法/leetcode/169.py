class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        for i in range(len(nums)):
            cache[nums[i]] = cache[nums[i]] + 1 if nums[i] in cache else 1
            if cache[nums[i]] > len(nums) // 2:
                return nums[i]



class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, cnt = 0, 0
        for num in nums:
            if cnt == 0:
                ans = num
            if num != ans:
                cnt -= 1
            else:
                cnt += 1
        return ans

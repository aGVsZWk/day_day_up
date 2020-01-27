class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = set([i for i in range(len(nums)+1)])
        for num in nums:
            cache.remove(num)
        return list(cache)[-1]

# 其它思路：求和，异或

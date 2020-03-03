class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.numsCache = []
        numsSum = 0
        for idx in range(len(nums)):
            numsSum += nums[idx]
            self.numsCache.append(numsSum)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > 0:
            return self.numsCache[j] - self.numsCache[i-1]
        else:
            return self.numsCache[j]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.numsCache = [0] + nums
        for i in range(1, len(self.numsCache)):
            self.numsCache[i] = self.numsCache[i-1] + nums[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.numsCache[j+1] - self.numsCache[i]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

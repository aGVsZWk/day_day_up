class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        numsSet = set()
        existNumsSet = set()
        for num in nums:
            if num - k in numsSet:
                existNumsSet.add(num)
            numsSet.add(num)
        return len(existNumsSet)


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        numsSet = set()
        answers = {}
        for num in nums:
            if num - k in numsSet:
                answers[num-k] = num
            if num + k in numsSet:
                answers[num] = num + k
            numsSet.add(num)
        return len(answers)

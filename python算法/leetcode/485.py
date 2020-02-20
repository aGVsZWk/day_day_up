class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        times = 0
        for num in nums:
            if num == 1:
                times += 1
                answer = max(answer, times)
            else:
                times = 0
        return answer


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        times = 0
        for num in nums:
            if num == 1:
                times += 1
            else:
                answer = max(answer, times)
                times = 0
        answer = max(answer, times)
        return answer

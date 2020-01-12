class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        queue = []
        t = 0
        for i in nums:
            if i < 1:
                queue.insert(0, i)
                t += 1
            elif i > 1:
                queue.append(i)
            else:
                queue.insert(t, i)
        nums[:] = queue

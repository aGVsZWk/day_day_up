class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j] == val:
                j += 1
            if j >= len(nums):
                return i
            nums[i] = nums[j]
            j += 1
            if j >= len(nums):
                return i + 1




class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

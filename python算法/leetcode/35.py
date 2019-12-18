class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)
        elif nums[0] > target:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i] >= target:
                    return i

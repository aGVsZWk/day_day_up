class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i, j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        knownNums = {}
        for index, data in enumerate(nums):
            anotherNum = target - data
            if anotherNum in knownNums:
                if knownNums[anotherNum] != index:
                    return [index, knownNums[anotherNum]]
            knownNums[data] = index

# 注意：数组中数字重复，往字典中添加的顺序问题

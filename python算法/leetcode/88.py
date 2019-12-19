class Solution:
    def insert(self, nums, index, val):
        for i in range(len(nums) - 1, index, -1):
            nums[i] = nums[i-1]
        nums[index] = val
        return nums
if __name__ == '__main__':
    s = Solution()
    a = s.insert([1, 2, 3, 4], 2, 100)
    print(a)

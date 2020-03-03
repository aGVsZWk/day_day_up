def shellSort(nums):
    step = len(nums) // 2
    while step > 0:
        for j in range(step, len(nums)):
            key = nums[j]
            i = j - step
            while i >= 0 and nums[i] > key:
                nums[i+step] = nums[i]
                i -= step
            nums[i+step] = key
        step //= 2

if __name__ == '__main__':
    nums = [1, 5, 6, 4, 2, 3, 3]
    shellSort(nums)
    nums

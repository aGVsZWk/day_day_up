def selectSort(nums):
    for i in range(0, len(nums)-1):
        t = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[t]:
                t = j
        nums[i], nums[t] = nums[t], nums[i]

if __name__ == '__main__':
    nums = [1, 5, 6, 4, 2, 3]
    selectSort(nums)
    nums

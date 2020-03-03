def quickSort(nums, p, r):
    if p < r:
        q = partition(nums, p, r)
        quickSort(nums, p, q-1)
        quickSort(nums, q+1, r)


def partition(nums, start, end):
    key = nums[end]
    i = start - 1
    for j in range(start, end):
        if nums[j] <= key:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[end] = nums[end], nums[i+1]
    return i + 1


if __name__ == '__main__':
    nums = [1, 5, 6, 4, 2, 3]
    quickSort(nums, 0, len(nums)-1)
    nums

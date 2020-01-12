# def quickSort(nums, p, r):
#     if p < r:
#         q = partition(nums, p, r)
#         quickSort(nums, p, q-1)
#         quickSort(nums, q+1, r)
#
# def partition(nums, p, r):
#     key = nums[r]
#     j = p
#     for i in range(p, r):
#         if nums[i] < key:
#             nums[i], nums[j] = nums[j], nums[i]
#             j += 1
#     nums[j], nums[r] = nums[r], nums[j]
#     return j

def quickSort(nums, p, r):
    if p < r:
        q = partition(nums, p, r)
        quickSort(nums, p, q-1)
        quickSort(nums, q+1, r)

def partition(nums, p, r):
    key = nums[r]
    j = p - 1
    for i in range(p, r):
        if nums[i] <= key:
            j += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[j+1], nums[r] = nums[r], nums[j+1]
    return j + 1


if __name__ == '__main__':
    a = [9, 5, 6, 4, 2, 3]
    quickSort(a, 0, len(a)-1)
    print(a)

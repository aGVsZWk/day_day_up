def mergeSort(nums, p, r):
    if p < r:
        q = (p + r)// 2
        mergeSort(nums, p, q)
        mergeSort(nums, q+1, r)
        merge(nums, p, q, r)

def merge(nums, p, q, r):
    import copy
    l1 = copy.copy(nums[p: q+1])
    l2 = copy.copy(nums[q+1: r+1])
    l1.append(float('inf'))
    l2.append(float('inf'))
    i, j = 0, 0
    for k in range(p, r+1):
        if l1[i] <= l2[j]:
            nums[k] = l1[i]
            i += 1
        else:
            nums[k] = l2[j]
            j += 1

if __name__ == '__main__':
    nums = [1, 5, 6, 4, 2, 3, 0]
    mergeSort(nums, 0, len(nums)-1)
    nums

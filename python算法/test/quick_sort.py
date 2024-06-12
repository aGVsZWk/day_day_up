# -*- coding: utf-8 -*-
# @Author: helei
# @Date:   2021-01-14
# @Email:  v_heleihe@tencent.com
# @Filename: quick_sort.py
# @Last modified by:   helei
# @Last modified time: 2021-01-14
def quick_sort(nums, p, r):
    if p < r:
        q = partition(nums, p, r)
        quick_sort(nums, p, q-1)
        quick_sort(nums, q+1, r)

def partition(nums, p, r):
    key = nums[r]
    i = p - 1
    for j in range(p, r):
        if nums[j] < key:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i+1

if __name__ == '__main__':
    nums = [1, 5, 6, 4, 2, 3]
    quick_sort(nums, 0, len(nums)-1)
    nums

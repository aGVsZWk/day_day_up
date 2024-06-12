# -*- coding: utf-8 -*-
# @Author: helei
# @Date:   2021-01-13
# @Email:  v_heleihe@tencent.com
# @Filename: qiuck_sort.py
# @Last modified by:   helei
# @Last modified time: 2021-01-13

def quick_sort(nums, p, r):
    if p < r:
        q = partition(nums, p, r)
        quick_sort(nums, p, q-1)
        quick_sort(nums, q+1, r)

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
    quick_sort(nums, 0, len(nums)-1)
    nums

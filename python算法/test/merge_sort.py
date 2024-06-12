# -*- coding: utf-8 -*-
# @Author: helei
# @Date:   2021-01-13
# @Email:  v_heleihe@tencent.com
# @Filename: merge_sort.py
# @Last modified by:   helei
# @Last modified time: 2021-01-13
import copy
def merge_sort(nums, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(nums, p, q)
        merge_sort(nums, q+1, r)
        merge(nums, p, q, r)

def merge(nums, p, q, r):
    l1 = copy.copy(nums[p:q+1])
    l2 = copy.copy(nums[q+1:r+1])
    l1.append(float('inf'))
    l2.append(float('inf'))
    k = 0
    j = 0
    for i in range(p, r+1):
        if l1[j] < l2[k]:
            nums[i] = l1[j]
            j += 1
        else:
            nums[i] = l2[k]
            k += 1

if __name__ == '__main__':
    nums = [1, 5, 6, 4, 2, 3]
    merge_sort(nums, 0, len(nums)-1)
    nums

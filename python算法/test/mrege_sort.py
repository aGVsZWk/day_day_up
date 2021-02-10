# -*- coding: utf-8 -*-
# @Author: helei
# @Date:   2021-01-14
# @Email:  v_heleihe@tencent.com
# @Filename: mrege_sort.py
# @Last modified by:   helei
# @Last modified time: 2021-01-14
import copy
def merge_sort(nums, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(nums, p, q)
        merge_sort(nums, q+1, r)
        merge(nums, p, q, r)

def merge(nums, p, q, r):
    l1 = nums[p:q+1]
    l2 = nums[q+1:r+1]
    t1 = copy.copy(l1)
    t2 = copy.copy(l2)
    t1.append(float('inf'))
    t2.append(float('inf'))
    j = 0
    k = 0
    for i in range(p, r+1):
        if t1[j] > t2[k]:
            nums[i] = t2[k]
            k += 1
        else:
            nums[i] = t1[j]
            j += 1

if __name__ == '__main__':
    nums = [1, 5, 6, 4, 2, 3]
    merge_sort(nums, 0, len(nums)-1)
    nums

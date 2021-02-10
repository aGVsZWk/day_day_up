# -*- coding: utf-8 -*-
# @Author: helei
# @Date:   2021-01-14
# @Email:  v_heleihe@tencent.com
# @Filename: insert_sort.py
# @Last modified by:   helei
# @Last modified time: 2021-01-14
def insert_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key


if __name__ == '__main__':
    nums = [1, 5, 6, 4, 2, 3]
    insert_sort(nums)
    nums

# -*- coding: utf-8 -*-
# @Author: helei
# @Date:   2021-01-14
# @Email:  v_heleihe@tencent.com
# @Filename: bullet_sort.py
# @Last modified by:   helei
# @Last modified time: 2021-01-14
def bullet_sort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    nums = [1, 5, 6, 4, 2, 3]
    bullet_sort(nums)
    nums

#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/16 7:14 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    0~n-1组成的数组中找出重复的任意一个数字。
    >>> duplicate([2, 3, 1, 0, 2, 5, 3])
    (True, 2)

    # test second
    # >>> find_duplicate([2, 3, 5, 4, 3, 2, 6, 7])
    # 3
    >>> find_duplicate([2, 3, 5, 4, 1, 2, 6, 7])
    2
"""


def duplicate(nums: list) -> int:
    for i, num in enumerate(nums):
        while i != num:
            if num == nums[num]:
                return True, num
            else:
                nums[i], nums[num] = nums[num], nums[i]
                num = nums[i]

    return False, None


def find_duplicate(nums: list) -> int:
    """
    不能修改原数组，范围为1~n
    时间复杂度:O(nlogn)
    空间复杂度:O(1)
    """
    def count_range(i, j):
        return sum(i<=num<=j for num in nums)

    lo = 1
    hi = len(nums) - 1     # n为范围
    while lo <= hi:
        mid = (lo + hi) // 2
        # print(lo, mid, hi)
        count = count_range(lo, mid)
        if lo == hi:
            if count > 1:
                return lo
            else:
                break
        if count > mid-lo+1:
            hi = mid
        else:
            lo = mid + 1
    return -1



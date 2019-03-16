#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 6:44 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    0~n中缺失的数字
    >>> nums = [0, 1, 2, 3, 5, 6]
    >>> find_missing(nums)
    4
    >>> random.shuffle(nums)
    >>> missingNumber(nums)
    4

    >>> missingNumber2(nums)
    4
"""

import random

def find_missing(nums: list) -> int:
    """
    解法1：限定有序的情况
    """
    l, r = 0, len(nums)-1
    while l < r:
        mid = (l+r) // 2
        if nums[mid] == mid:
            l = mid + 1
        else:
            r = mid
    return nums[r]-1


def missingNumber(nums: list) -> int:
    """
    解法2：数学公式。
    """
    n = len(nums)
    expected_sum = n*(n+1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


def missingNumber2(nums: 'List[int]') -> 'int':
    """
    解法3：异或
    """
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing
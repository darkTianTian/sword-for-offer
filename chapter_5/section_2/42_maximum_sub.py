#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 5:17 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    连续子数组的最大和
    >>> nums = [1, -2, 3, 10, -4, 7, 2, -5]
    >>> maxSubArray(nums)
    18
    >>> maxSubArray2(nums)
    18
"""

def maxSubArray(nums: list) -> int:
    """
    解法1：书中的思想
    """
    cp_nums = nums[:]
    for i in range(1, len(nums)):
        if cp_nums[i-1] > 0:
            cp_nums[i] += cp_nums[i-1]
    return max(cp_nums)


def maxSubArray2(nums: list) -> int:
    """
    解法2：同1，简便写法。
    """
    from itertools import accumulate
    return max(accumulate(nums, lambda x, y: x+y if x > 0 else y))
#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 7:48 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    滑动窗口的最大值。
    >>> nums = [2, 3, 4, 2, 6, 2, 5, 1]
    >>> maxInWindows(nums, 3)
    [4, 4, 6, 6, 6, 5]

"""


def maxInWindows(nums: list, size: int) -> int:
    return [max(nums[i:i+size])
            for i in range(len(nums)-size+1) if size!=0 ]
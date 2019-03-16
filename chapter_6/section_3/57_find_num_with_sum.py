#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 7:44 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    找出和为s的数字。
    >>> nums = [1, 2, 4, 7, 11, 15]
    >>> FindNumbersWithSum(nums, 15)
    (4, 11)
"""

def FindNumbersWithSum(array: list, tsum: int) -> tuple:
    l, r = 0, len(array)-1
    while l < r:
        if array[l] + array[r] < tsum:
            l += 1
        elif array[l]+array[r] > tsum:
            r -= 1
        else:
            return array[l], array[r]
    return []
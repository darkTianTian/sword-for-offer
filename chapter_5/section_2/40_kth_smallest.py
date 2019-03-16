#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 5:06 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    最小的K个数
    >>> nums = [4, 5, 1, 2, 6, 7, 3, 8]
    >>> GetSmallNumbers_Solution(nums, 4)
    [1, 2, 3, 4]
"""


def GetSmallNumbers_Solution(tinput: list, k: int) -> list:
    # write code here
    l, r = 0, len(tinput) - 1
    if k > len(tinput) or k < 1: return []  # for passing the damn testcases in niuke
    while True:
        pos = partition(tinput, l, r)
        if pos < k - 1:
            l = pos + 1
        elif pos > k - 1:
            r = pos - 1
        else:
            return sorted(
                tinput[:pos + 1])  # sorted for passing the damn testcases of niuke


def partition(nums: list, l: int, r: int) -> int:
    from random import randint
    p = randint(l, r)                   # 消除依赖
    nums[r], nums[p] = nums[p], nums[r]
    for i, v in enumerate(nums[l:r + 1], l):
        if nums[i] <= nums[r]:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
    return l - 1  # the pivot inde
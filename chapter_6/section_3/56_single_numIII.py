#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 7:27 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    数组中两个唯一出现一次的元素，其余均出现两次。
    >>> nums = [2, 4, 3, 6, 3, 2, 5, 5]
    >>> singleNumber(nums)
    (4, 6)
"""

# 思想：将这两个元素分到两个组，由于这两个数不相等，所以亦或结果不为0，
# 也就是说二进制中至少有一位1，记为第n位。我们以第n位是否为1，把数组分为两个子数组。


def singleNumber(nums: list) -> tuple:
    total_xor = get_xor(nums)
    mask = 1
    while total_xor & mask == 0:
        mask <<= 1
    p1 = [num for num in nums if num & mask == 0]
    p2 = [num for num in nums if num & mask != 0]
    return get_xor(p1), get_xor(p2)


def get_xor(nums: list) -> int:
    from functools import reduce
    return reduce(lambda x, y: x ^ y, nums)
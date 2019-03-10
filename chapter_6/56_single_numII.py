#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 7:35 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    找出数组中出现一次的元素，其它元素出现三次。
    >>> nums = [1, 2, 3, 2, 2, 1, 1, 4, 4, 4]
    >>> single_number(nums)
    3
"""


def single_number(nums: list, n=3) -> int:
    ans = 0
    for i in range(32):
        count = 0
        for num in nums:
            if ((num >> i) & 1):
                count += 1
        ans |= ((count%n!=0) << i)
    return convert(ans)

def convert(x):
    if x >= 2**31:
        x -= 2**32
    return x
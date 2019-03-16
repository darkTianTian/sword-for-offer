#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 5:26 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    把数组排成最小的数字
    >>> nums = [3, 32, 321]
    >>> PrintMinNumber(nums)
    '321323'
"""

from functools import cmp_to_key

def PrintMinNumber(numbers):
    nums = list(map(str, numbers))
    nums.sort(key=cmp_to_key(lambda x, y: ((x+y)>(y+x)) - ((y+x)>(x+y))))
    return ''.join(nums)
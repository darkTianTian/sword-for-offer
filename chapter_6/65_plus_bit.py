#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 8:12 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    不用加减乘除做加法。
    >>> getSum(1, 2)
    3
    >>> a, b = 2**31, (-2**5)
    >>> getSum2(a, b) == a+b
    True
    >>> getSum2(-12, -8)
    -20
    >>> getSum(9, -18)
    -9

"""

import numpy as np

def getSum(a: int, b: int) -> int:

    while b != 0:
        a, b = np.int32(a ^ b), np.int32((a & b) << 1)
    return int(a)



def getSum2(a, b):
    # 32 bits integer max
    MAX = 0x7FFFFFFF  # 2**31-1
    # 32 bits interger min
    MIN = 0x80000000  # -2**31
    # mask to get last 32 bits
    mask = 0xFFFFFFFF  # 2*32-1
    while b != 0:
        # ^ get different bits and & gets double 1s, << moves carry
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    # if a is negative, get a's 32 bits complement positive first
    # then get 32-bit positive's Python complement negative
    return a if a <= MAX else ~(a ^ mask)
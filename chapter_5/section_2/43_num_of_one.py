#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 5:21 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    1~n整数中1出现的次数。
    >>> countDigitOne(12)
    5
"""


def countDigitOne(n: int) -> int:
    counter, i = 0, 1
    while i <= n:
        divider = i * 10
        counter += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
        i *= 10
    return counter

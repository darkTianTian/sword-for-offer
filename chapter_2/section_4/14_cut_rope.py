#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 4:44 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    剪绳子
    >>> cut_rope(8)
    18
"""


def cut_rope(length: int) -> int:
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    # 尽可能剪出3
    timesOf3 = length // 3
    # 如果最后余1，则留一段4分成两半
    if length - timesOf3 * 3 == 1:
        timesOf3 -= 1
    timesOf2 = (length - timesOf3 * 3) // 2
    return (3 ** timesOf3) * (2 ** timesOf2)
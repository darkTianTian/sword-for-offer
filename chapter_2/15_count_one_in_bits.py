#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 4:50 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    二进制中1的个数
    >>> hamming_weigth(11)
    3
    >>> all(bin(n).count('1')==hamming_weigth(n) for n in range(30))
    True
"""


def hamming_weigth(n: int) -> int:
    """
    一个数n和它-1做与运算，就相当于干掉了最右边的1.
    """
    bits = 0
    while n:
        bits += 1
        n = (n-1) & n
    return bits
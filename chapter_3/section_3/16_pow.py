#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 5:04 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    实现pow函数
    >>> my_pow(2, 10)
    1024
    >>> a, b = randint(-10, 10), randint(10, 10)
    >>> c = int(math.pow(a, b))
    >>> d = my_pow(a, b)
    >>> c == d
    True
"""

from random import randint
import math


def my_pow(x: int, n: int):
    if n < 0:
        return 1 / pow_with_unsigned(x, -n)
    else:
        return pow_with_unsigned(x, n)


def pow_with_unsigned(x: int, n: int):
    if n == 1:
        return x
    if n == 0:
        return 1

    res = pow_with_unsigned(x, n >> 1)
    res *= res

    if n & 1 == 1:
        res *= x

    return res
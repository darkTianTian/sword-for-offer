#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 4:00 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    斐波那契数列
    >>> fibonacci(3)
    3
    >>> fibonacci(5)
    8
    >>> fibonacci2(5)
    8
    >>> fibonacci2(30)
    1346269
"""

import functools


def fibonacci(n: int) -> int:
    a = b = 1
    for _ in range(n-1):
        a, b = b, a+b
    return b

@functools.lru_cache()
def fibonacci2(n: int) -> int:
    """
    递归时注意使用备忘，否则将计算多次fibonacci2(1)
    """
    if n < 2:
        return 1
    return fibonacci2(n-1) + fibonacci2(n-2)




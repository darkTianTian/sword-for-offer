#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 5:32 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    丑数
    >>> nthUglyNumber(5)
    5
    >>> nthUglyNumber(1)
    1
    >>> nthUglyNumber(4)
    4
    >>> nthUglyNumber(1500)
    859963392
"""


def nthUglyNumber(n: int) -> int:
    """
    书中的解法
    """
    q = [1]
    t2, t3, t5 = 0, 0, 0
    for i in range(n-1):
        a2, a3, a5 = q[t2]*2, q[t3]*3, q[t5]*5
        to_add = min(a2, a3, a5)
        q.append(to_add)
        if a2 == to_add:
            t2 += 1
        if a3 == to_add:
            t3 += 1
        if a5 == to_add:
            t5 += 1
    return q[-1]
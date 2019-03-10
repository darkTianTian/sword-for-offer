#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 8:04 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
   圆圈中最后剩下的数字
   >>> LastRemaining_Solution(5, 3)
   3
"""


def LastRemaining_Solution(n: int, m: int) -> int:
    if n<=0 or m<=0:
        return -1
    last_num = 0
    for i in range(2, n+1):
        last_num = (last_num+m) % i
    return last_num
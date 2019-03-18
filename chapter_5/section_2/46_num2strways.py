#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/18 2:46 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    数字翻译成字符串有多少种
    >>> num_decodings('226')
    3
"""



def num_decodings(s: str) -> int:
    # w tells the number of ways
    # v tells the previous number of ways
    # d is the current digit
    # p is the previous digit
    v, w, p = 0, int(s>''), ''
    for d in s:
        v, w, p = w, int(d>'0')*w + (9<int(p+d)<27)*v, d
    return w
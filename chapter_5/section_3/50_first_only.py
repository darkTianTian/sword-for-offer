#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 5:36 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    第一个只出现一次的字符
    >>> s = 'google'
    >>> firstUniqChar(s)
    'l'
"""

def firstUniqChar(s: str) -> str:
    from collections import Counter
    c = Counter(s)
    for i, ch in enumerate(s):
        if c[ch] == 1:
            return ch
    return ''
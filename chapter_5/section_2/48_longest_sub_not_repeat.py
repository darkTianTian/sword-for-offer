#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 5:28 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    最长不含重复字符的子字符串

    >>> s = 'arabcacfr'
    >>> lengthOfLongestSubstring(s)
    4
    >>> lengthOfLongestSubstring('abba')
    2

"""


def lengthOfLongestSubstring(s: str) -> str:
    res, start = 0, 0
    dic = {}
    for end in range(len(s)):
        if s[end] in dic:
            start = max(start, dic[s[end]]+1)
            # start = dic[s[end]] + 1
        dic[s[end]] = end
        res = max(res, end-start+1)
    return res
#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 4:38 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    字符串的全排列，可能包含重复的字符，因此要去重。
    >>> s1 = 'abc'
    >>> s2 = 'aacd'
    >>> ans1 = sorted(list(set(''.join(x) for x in permutations(s1))))
    >>> ans2 = sorted(list(set(''.join(x) for x in permutations(s2))))
    >>> ans1 == my_permutation(s1)
    True
    >>> ans2 == my_permutation(s2)
    True
"""

from itertools import permutations

def my_permutation(ss: str) -> 'List[str]':
    ans = ['']
    for s in ss:
        ans = [p[:i] + s + p[i:]
               for p in ans for i in range((p+s).index(s)+1)]
    return sorted(ans) if ss else []
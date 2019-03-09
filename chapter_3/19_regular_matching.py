#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 5:32 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    正则表达式匹配
    >>> match('aaa', 'a.a')
    True
    >>> match('aaa', 'ab*ac*a')
    True
    >>> match('aaa', 'aa.a')
    False
    >>> match('aaa', 'ab*a')
    False
"""

def match(s: str, pattern: str) -> 'bool':
    if not pattern: return not s
    f_match = bool(s) and pattern[0] in {s[0], '.'}
    # 一定要用bool(s)，否则会输出''，牛客网又忽略了这个TestCase
    if len(pattern) > 1 and pattern[1] == '*':
        return (match(s, pattern[2:]) or
                (f_match and match(s[1:], pattern)))
    else:
        return f_match and match(s[1:], pattern[1:])
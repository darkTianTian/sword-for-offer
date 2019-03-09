#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 2:26 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    替换空格
    >>> s = 'We are happy.'
    >>> replace_space(s)
    'We%20are%20happy.'
    >>> s1 = 'We are very  happy!'
    >>> replace_space(s1)
    'We%20are%20very%20%20happy!'
"""

def replace_space(s: str) -> str:
    return ''.join(c if c!=' ' else '%20' for c in s)

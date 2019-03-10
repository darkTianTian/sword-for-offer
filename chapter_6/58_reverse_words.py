#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 7:46 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    反转一句话的单词。
    >>> s = "the sky is blue"
    >>> reverse_words(s)
    'blue is sky the'
"""

def reverse_words(s: str) -> str:
    return ' '.join(s.split()[::-1])
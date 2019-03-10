#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 8:10 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    求1+...n， 不能用循环等。
    >>> sum_solution(10)
    55
"""




def sum_solution(n: int) -> int:
    return n and (n+sum_solution(n-1))
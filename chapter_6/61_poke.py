#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 8:02 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    扑克牌中的顺子。
    >>> nums = [0, 0, 1, 2, 3]
    >>> IsContinuous(nums)
    True
    >>> nums2 = [3, 4, 6, 8, 0]
    >>> IsContinuous(nums2)
    False
"""


def IsContinuous(numbers: list) -> 'bool':

    if not numbers:
        return False
    joker_count = numbers.count(0)
    left_cards = sorted(numbers)[joker_count:]
    need_joker = 0
    for i in range(len(left_cards)-1):
        if left_cards[i+1] == left_cards[i]:
            return False
        need_joker += (left_cards[i+1]-left_cards[i]-1)
    return need_joker <= joker_count
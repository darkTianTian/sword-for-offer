#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 8:08 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    股票的最大利润
    >>> prices = [9, 11, 8, 5, 7, 12, 16, 14]
    >>> maxProfit(prices)
    11
"""

def maxProfit(prices: 'List[int]') -> int:
    ans, min_buy = 0, float('inf')
    for price in prices:
        if price < min_buy:
            min_buy = price
        elif price-min_buy > ans:
            ans = price - min_buy
    return ans
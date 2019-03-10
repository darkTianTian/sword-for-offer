#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 5:11 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    找出数据流中的中位数。
    >>> mf = MedianFinder()
    >>> mf.addNum(41)
    >>> mf.findMedian()
    41.0
    >>> mf.addNum(35)
    >>> mf.findMedian()
    38.0
    >>> mf.addNum(62)
    >>> mf.addNum(4)
    >>> mf.addNum(97)
    >>> mf.findMedian()
    41.0
"""

import heapq as hq


class MedianFinder:

    def __init__(self):
        self.lo, self.hi = [], []  # lo is max_heap, hi is min_heap

    def addNum(self, num: int):
        hq.heappush(self.lo, -num)
        hq.heappush(self.hi, -hq.heappop(self.lo))

        if len(self.lo) < len(self.hi):
            hq.heappush(self.lo, -hq.heappop(self.hi))

    def findMedian(self):
        if len(self.lo) == len(self.hi):
            return (-self.lo[0] + self.hi[0]) / 2.0
        else:
            return float(-self.lo[0])
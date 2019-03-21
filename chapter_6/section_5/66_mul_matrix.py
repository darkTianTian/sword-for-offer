#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/21 1:10 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    构建乘积数组
    >>> multiply(list(range(1, 6)))
    [120, 60, 40, 30, 24]
    >>> a = multiply(list(range(4, 10)))
    >>> b = check(list(range(4, 10)))
    >>> a == b
    True
    >>> multiply([1, 2, 3, 0, 5])
    [0, 0, 0, 30, 0]
    >>> multiply([1, 0, 3, 0, 5])
    [0, 0, 0, 0, 0]
"""

from itertools import accumulate
from operator import mul
from functools import reduce
import random

def multiply(A: list) -> list:
    from itertools import accumulate
    from operator import mul
    C = [1] # 第一个元素相当于没有
    C += accumulate(A[:-1], mul)    # `+=`支持右边生成器，`+`不支持
    D = [1]
    D += accumulate(A[:0:-1], mul)
    D.reverse()
    return [C[i] * D[i] for i in range(len(A))]


def check(A):

    def helper_mul(x, y):
        if x == 0:
            x = 1
        if y == 0:
            y = 1
        return x * y

    print(A, A.count(0))
    if A.count(0) > 1:
        return [0] * len(A)

    total = reduce(helper_mul, A)
    has_0 = 0 in A
    ans = []
    for num in A:
        if num == 0:
            ans.append(total)
        elif has_0:
            ans.append(0)
        else:
            ans.append(total // num)

    return ans

if __name__ == '__main__':

    for _ in range(1000):

        a = random.sample(range(1, 15), 3)
        b = random.sample(range(-10, 20), 1)
        d = random.sample(range(-5, 5), 1)
        c = a + b + d
        # c = [0, 2, 3, 5]
        ans1 = multiply(c)
        ans2 = check(c)
        print(ans1, ans2)
        assert ans1 == ans2

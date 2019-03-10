#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 7:50 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    n个骰子的点数。
    >>> dice_probability_dict(1)
    {1: 0.16667, 2: 0.16667, 3: 0.16667, 4: 0.16667, 5: 0.16667, 6: 0.16667}
    >>> ans = dice_probability_dict(2)
    >>> for k, v in ans.items():    # doctest: +ELLIPSIS
    ...     print(k, v)
    2 0.02778
    3 0.05556
    4 0.08333
    5 0.11111
    6 0.13889
    ...

"""

def dice_probability_dict(n: int, val=6) -> dict:
    from collections import defaultdict
    dp = defaultdict(int)
    dp.update({k: 1 for k in range(1, val+1)})  # 初始化第一个骰子
    for i in range(n-1):  # 根据第i个骰子更新第i+1个骰子
        new_dp = defaultdict(int)
        for j in range(n*(i+1), val*n+1):  # n个骰子最小值为n*(i+1)，最大值为val*n
            # 第i+1个骰子和为j（实际为j+1，因为数组下标从0开始）的次数，等于第i个
            # 骰子j-1 ~ j-6次数的总和
            new_dp[j] = sum(dp[j-k] for k in range(1, val+1))
        dp = new_dp

    # 这时的dp就是得到我们想要的了，只不过值为出现的次数，我们算一下概率
    count = {k: round(float(times / (val**n)), 5)
             for k, times in dp.items()}
    return count
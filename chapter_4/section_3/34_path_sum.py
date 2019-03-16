#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 11:26 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    返回二叉树中路径和为某一值得所有路径。
    >>> t1 = '10,5,4,$,$,7,$,$,12,$,$'
    >>> t1 = deserialize_tree(t1)
    >>> pathSum(t1, 22)
    [[10, 5, 7], [10, 12]]
"""

from utils import deserialize_tree

def pathSum(root: 'TreeNode', sum: int) -> 'List[List[int]]':
    if not root:
        return []
    val, *kids = root.val, root.left, root.right
    if any(kids):
        return [[val] + path
                for kid in kids if kid
                for path in pathSum(kid, sum-val)]
    return [[val]] if val==sum else []

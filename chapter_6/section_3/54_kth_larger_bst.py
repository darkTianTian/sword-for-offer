#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 6:52 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    二叉搜索树的第K大节点
    >>> t1 = '5,3,2,$,$,4,$,$,7,6,$,$,8,$,$'
    >>> t1 = deserialize_tree(t1)
    >>> kth_largest(t1, 2)
    7
"""

from utils import deserialize_tree

def kth_largest(root: 'TreeNode', k: int) -> int:
    """
    牛客网是求最小，比较简单，书中求最大，那么只要将中序遍历的左右互换。
    """
    stack, ans = [], None
    while True:
        while root:
            stack.append(root)
            root = root.right
        cur = stack.pop()
        k -= 1
        ans = cur.val
        root = cur.left
        if k == 0:
            return ans
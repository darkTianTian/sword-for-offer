#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 11:05 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    从上到下打印二叉树
    >>> t1 = '8,6,5,$,$,7,$,$,10,9,$,$,11,$,$'
    >>> t1 = deserialize_tree(t1)
    >>> PrintFromTopToBottom(t1)
    [8, 6, 10, 5, 7, 9, 11]
    >>> levelOrder(t1)
    [[8], [6, 10], [5, 7, 9, 11]]
    >>> zigzagLevelOrder(t1)
    [[8], [10, 6], [5, 7, 9, 11]]
"""

from utils import deserialize_tree


# 从上到下打印
def PrintFromTopToBottom(root: 'TreeNode') -> list:
    from collections import deque
    queue = deque([root])
    res = []
    while queue:
        cur = queue.popleft()
        if cur:
            res.append(cur.val)
            queue.append(cur.left)
            queue.append(cur.right)
    return res

# 分层打印
def levelOrder(root: 'TreeNode') -> 'List[List[int]]':
    ans, level = [], root and [root]
    while level:
        ans.append([n.val for n in level])
        level = [k for n in level for k in (n.left, n.right) if k]
    return ans

# 之字形打印
def zigzagLevelOrder(root: 'TreeNode') -> 'List[List[int]]':
    ans, level, order = [], root and [root], 1
    while level:
        ans.append([n.val for n in level][::order])
        order *= -1
        level = [kid for n in level for kid in (n.left, n.right) if kid]
    return ans
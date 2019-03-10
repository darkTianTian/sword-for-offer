#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 7:04 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    判断是否为平衡二叉树
    >>> t1 = '1,2,4,$,$,5,7,$,$,$,3,$,6,$,$'
    >>> t1 = deserialize_tree(t1)
    >>> isBalanced(t1)
    True
    >>> t2 = '1,2,4,$,$,5,7,8,$,$,$,$,3,$,6,$,$'
    >>> t2 = deserialize_tree(t2)
    >>> isBalanced(t2)
    False
    >>> is_balanced2(t1)
    True
    >>> is_balanced2(t2)
    False
"""

from collections import defaultdict

from utils import deserialize_tree

def isBalanced(root: 'TreeNode') -> 'bool':

    """
    解法1：深度遍历。
    """
    balanced = True

    def dfs(node):
        nonlocal  balanced
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        if not balanced or abs(left - right) > 1:
            balanced = False
        return max(left, right) + 1

    dfs(root)
    return balanced

def is_balanced2(root: 'TreeNode') -> 'bool':
    """
    解法2：后序遍历
    """
    stack, node = [], root
    last, depths = None, defaultdict(int)
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            if not node.right or last == node.right:
                node = stack.pop()
                left, right  = depths[node.left], depths[node.right]
                if abs(left - right) > 1:
                    return False
                depths[node] = 1 + max(left, right)
                last, node = node, None
            else:
                node = node.right
    return True

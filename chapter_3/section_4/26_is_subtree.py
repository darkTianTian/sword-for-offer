#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 7:45 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    是否是树的子结构
    >>> t1 = '8,8,9,$,$,2,4,$,$,7,$,$,7,$,$'
    >>> t1 = deserialize_tree(t1)
    >>> t2 = '8,9,$,$,2,$,$'
    >>> t2 = deserialize_tree(t2)
    >>> is_subtree(t1, t2)
    True

    >>> t1 = TreeNode(1)
    >>> t1.left, t1.right = TreeNode(2), TreeNode(3)
    >>> t1.left.left = TreeNode(4)
    >>> t2 = TreeNode(2)
    >>> t2.left = TreeNode(5)
    >>> is_subtree(t1, t2)
    False
"""

from utils import TreeNode, deserialize_tree

#  注意：此题和LeetCode中572不一样，572中
#     3
#    / \
#   4   5
#  / \
# 1   2
#    /
#   0

#   和子树，返回值为False，因为2还有左子树。而书中则认为是True。
#   4
#  / \
# 1   2



def is_subtree(s: 'TreeNode', t: 'TreeNode') -> 'bool':

    def is_same(t1, t2):
        if not t2:
            return True
        if not t1:
            return False
        return t1.val == t2.val and is_same(t1.left, t2.left) and is_same(t1.right, t2.right)

    if not s or not t: return False
    stack = s and [s]
    while stack:
        node = stack.pop()
        if node:
            if is_same(node, t):
                return True
            stack.append(node.right)
            stack.append(node.left)
    return False

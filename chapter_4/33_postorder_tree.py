#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 11:13 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    二叉树后序遍历
    >>> t1 = '8,6,5,$,$,7,$,$,10,9,$,$,11,$,$'
    >>> t1 = deserialize_tree(t1)
    >>> postorder_traversal(t1)
    [5, 7, 6, 9, 11, 10, 8]
    >>> postorder_traversal2(t1)
    [5, 7, 6, 9, 11, 10, 8]
    >>> postorder_traversal3(t1)
    [5, 7, 6, 9, 11, 10, 8]
    >>> postorder_traversal4(t1)
    [5, 7, 6, 9, 11, 10, 8]
"""

from utils import deserialize_tree

def postorder_traversal(root: 'TreeNode') -> list:
    """
    解法1：根右左，再倒序。
    """
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
    return res[::-1]


def postorder_traversal2(root: 'TreeNode') -> list:
    """
    解法2：使用元组的形式判断当前节点是否访问过
    """
    res, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                res.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
    return res


def postorder_traversal3(root: 'TreeNode') -> list:
    """
    解法3：空间复杂度最低的方法。
    """
    res, stack, node, last = [], [], root, None
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            if not node.right or last == node.right:
                node = stack.pop()
                res.append(node.val)
                last, node = node, None
            else:
                node = node.right
    return res


def postorder_traversal4(root: 'TreeNode') -> list:
    """
    解法4：生成器。
    """
    def dfs(node):
        if node:
            yield from dfs(node.left)
            yield from dfs(node.right)
            yield node.val

    return list(dfs(root))
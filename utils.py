#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 2:37 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


class ListNode:

    def __init__(self, x: int):
        self.val = x
        self.next = None

def construct_linklist(nodes: 'iterable')-> 'LinkedList':
    vals = list(nodes)
    head = ListNode(0)
    h = head
    for val in vals:
        h.next = ListNode(val)
        h = h.next
    return head.next

def pretty_linklist(head: 'LinkedList') -> str:
    ans = []
    h = head
    while h:
        ans.append(str(h.val))
        h = h.next
    return '->'.join(ans)


class TreeNode:

    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

def preorder_traversal(root: TreeNode) -> list:
    def dfs(node):
        if node:
            yield node.val
            yield from dfs(node.left)
            yield from dfs(node.right)

    return list(dfs(root))

def inorder_traversal(root: TreeNode) -> list:
    def dfs(node):
        if node:
            yield from dfs(node.left)
            yield node.val
            yield from dfs(node.right)

    return list(dfs(root))

def deserialize_tree(data):
    nodes = data.split(',')[::-1]
    return deserialize_tree_util(nodes)

def deserialize_tree_util(nodes):
    val = nodes.pop()
    if val == '$':
        return None
    root = TreeNode(int(val))
    root.left = deserialize_tree_util(nodes)
    root.right = deserialize_tree_util(nodes)
    return root

def is_same_tree(p: 'TreeNode', q: 'TreeNode') -> 'bool':
    if p and q:
        return (p.val==q.val and is_same_tree(p.left, q.left) and
                is_same_tree(p.right, q.right))
    else:
        return p is q
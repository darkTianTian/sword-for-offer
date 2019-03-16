### 22 链表中倒数第k个节点

思路：两个指针，快指针先走k-1步，然后两个一起走，快指针走到尾节点时，慢指针在倒数第k个节点。
需考虑k=0时和fast已经走到尾节点的情况。

```python
def FindKthToTail(self, head, k):
    fast = slow = head
    for _ in range(k):
        if fast:
            fast = fast.next
        else:
            return None
    while fast:
        slow, fast = slow.next, fast.next
    return slow
```

### 23 链表中环的入口节点
[LeetCode链接](https://leetcode.com/problems/linked-list-cycle-ii/description/)

* 首先判断此链表是否有环。
* 然后再相交点和头结点一起走，一定会在入口相遇。


```python
def detectCycle(self, head):        
    fast = slow = head
    # 检测是否有环
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            break
    else:
        return None
    # 找出入口节点
    while head is not slow:
        head, slow = head.next, slow.next
    return head
```

### 24 反转链表

```python
def reverseList(self, head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev
```

### 25 合并两个有序链表

方法1：iteratively 迭代

```python
def mergeTwoLists(l1, l2):
    l = head = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            l.next, l1 = l1, l1.next
        else:
            l.next, l2 = l2, l2.next
        l = l.next
    l.next = l1 or l2
    return head.next
```

方法2：recursively 递归

```python
def mergeTwoLists(l1, l2):
    # 判断是否存在None
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2
```

### 26 树的子结构

[LeetCode链接](https://leetcode.com/problems/subtree-of-another-tree/description/)

二刷的时候突然发现，此题和LeetCode中不同。LeetCode中子树`4-1-2`返回False因为2下边还有节点，所以不一样；而书中认为True，不考虑2下边的节点。

```
     3
    / \
   4   5
  / \
 1   2
    /
   0
```

```python
def is_subtree(s: 'TreeNode', t: 'TreeNode') -> 'bool':

    def is_same(s, t):
        if s and t:
            equal = s.val==t.val
            if not t.left and not t.right:
                return equal
            else:
                return (equal and is_same(s.left, t.left) and
                        is_same(s.right, t.right))
        else:
            return s is t
    stack = s and [s]
    while stack:
        node = stack.pop()
        if node:
            res = is_same(node, t)
            if res:
                return True
            stack.append(node.right)
            stack.append(node.left)
    return False
```
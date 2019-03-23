### 30 包含min函数的栈

#### [LeetCode传送门](https://leetcode.com/problems/min-stack/description/)

```python
class MinStack:

    def __init__(self):
        self._stack = []
        
    def push(self, x: int) -> None:
        cur_min = self.getMin()
        if x < cur_min:
            cur_min = x
        self._stack.append((x, cur_min))
        
    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        if not self._stack:
            return None
        else:
            return self._stack[-1][0]

    def getMin(self) -> int:
        if not self._stack:
            return float('inf')
        else:
            return self._stack[-1][1]
```

### 31 栈的压入、弹出序列

#### [LeetCode传送门](https://leetcode.com/problems/validate-stack-sequences/)

```python
def validateStackSequences(self, pushed: 'List[int]', popped: 'List[int]') -> 'bool':
    stack = []
    j = 0
    for num in pushed:
        stack.append(num)
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return j == len(popped)
```

### 32 从上到下打印二叉树

#### [牛客网传送门](https://www.nowcoder.com/practice/7fe2212963db4790b57431d9ed259701?tpId=13&tqId=11175&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
#### [AcWing传送门](https://www.acwing.com/problem/content/41/)

双端队列

```python
def PrintFromTopToBottom(self, root):
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
```

### 32_1 分层从上到下打印二叉树

#### [LeetCode传送门](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)

```python
def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
    ans, level = [], root and [root]
    while level:
        ans.append([n.val for n in level])
        level = [k for n in level for k in (n.left, n.right) if k]
    return ans
```

### 32_2 之字形打印二叉树

#### [LeetCode传送门](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/)

```python
def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
    ans, level, order = [], root and [root], 1
    while level:
        ans.append([n.val for n in level][::order])
        order *= -1
        level = [kid for n in level for kid in (n.left, n.right) if kid]
    return ans
```

### 33 是否是二叉搜索树的后序遍历

#### [牛客网传送门](https://www.nowcoder.com/practice/a861533d45854474ac791d90e447bafd?tpId=13&tqId=11176&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tPage=2)

```python
def VerifySquenceOfBST(self, seq):
    from itertools import takewhile
    if not seq:
        return False
    p = seq[-1]
    left_sub = list(takewhile(lambda x: x < p, seq[:-1]))
    right_sub = seq[len(left_sub):-1]
    if not all(x>p for x in right_sub):
        return False
    left = right = True
    if left_sub:
        left = self.VerifySquenceOfBST(left_sub)
    if right_sub:
        right = self.VerifySquenceOfBST(right_sub)
    return left and right
```
### 33_1 二叉树的后序遍历

#### [LeetCode传送门](https://leetcode.com/problems/binary-tree-postorder-traversal/description/)

方法一：根右左，再倒序。

```python
def postorder_traversal(root):
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
    return res[::-1]
```

方法二：思想: 使用`last`作为判断是否该节点的右子树完成遍历，如果一个`node.right`已经刚刚遍历完毕，那么将`last==node.right`，否则将会寻找`node.right`。

```python
def postorderTraversal(self, root):
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
```

方法三：使用boolean判断一个节点是否被遍历过

```python
def postorderTraversal(self, root):
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
```

方法四：dfs.

```python
def postorderTraversal(self, root: TreeNode) -> List[int]:

    def dfs(n):
        if n:
            yield from dfs(n.left)
            yield from dfs(n.right)
            yield n.val
    return list(dfs(root))
```

### 34 二叉树和为某一值的路径

#### [LeetCode传送门](https://leetcode.com/problems/path-sum-ii/description/)

```
sum = 22

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
[
   [5,4,11,2],
   [5,8,4,5]
]
```
<font color=#32CD32 size=3>方法一：iteratively. 举一反三。</font>

```python
def pathSum(self, root: 'TreeNode', total: 'int') -> 'List[List[int]]':
    stack = root and [(root, [root.val], total)]
    ans = []
    while stack:
        n, v, t = stack.pop()
        if not n.left and not n.right and n.val==t:
            ans.append(v)
        if n.right:
            stack.append((n.right, v+[n.right.val], t-n.val))
        if n.left:
            stack.append((n.left, v+[n.left.val], t-n.val))
    return ans
```

recursively. 先找出所有路径，再过滤，实际上和257题一样。不过这并没有把这道题的特性涵盖进去。

```python
def pathSum(self, root, sum_val):
    paths = self.all_paths(root)
    return [path for path in paths if sum(path)==sum_val]
    
def all_paths(self, root):
    if not root:
        return []
    return [[root.val]+path
            for kid in (root.left, root.right) if kid
            for path in self.all_paths(kid)] or [[root.val]]
```

<font color=#32CD32 size=3>方法三：recursively. </font>

```python
def pathSum(self, root, sum):
    if not root:
        return []
    val, *kids = root.val, root.left, root.right
    if any(kids):
        return [[val] + path
                for kid in kids if kid
                for path in self.pathSum(kid, sum-val)]
    return [[val]] if val==sum else []
```
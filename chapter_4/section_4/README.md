### 35 复杂链表的复制

#### [LeetCode传送门](https://leetcode.com/problems/copy-list-with-random-pointer/description/)

方法一：遍历两次。

```python
def copyRandomList(self, head: 'Node') -> 'Node':
    cp = {None: None}
    m = n = head
    while m:
        cp[m] = Node(m.val, None, None)
        m = m.next
    while n:
        cp[n].next = cp[n.next]
        cp[n].random = cp[n.random]
        n = n.next
    return cp[head]
```

Time-O(n), Memory-O(n). 这种方式是相当于把第一次迭代的过程委托给了`defaultdict`，通过创建一个默认的对象，再去修改它的label值。

```python
def copyRandomList(self, head: 'Node') -> 'Node':
    cp = collections.defaultdict(lambda: Node(0, None, None))
    cp[None] = None
    h = head
    while h:
        cp[h].val = h.val
        cp[h].next = cp[h.next]
        cp[h].random = cp[h.random]
        h = h.next
    return cp[head]
```

### 36 二叉搜索树与双向链表

#### LeetCode有此题，但是不是免费的。[牛客网传送门](https://www.nowcoder.com/practice/947f6eb80d944a84850b0538bf0ec3a5?tpId=13&tqId=11179&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
#### [AcWing传送门](https://www.acwing.com/problem/content/87/)

方法一：中序遍历，再构造链表。

```python
def convert(self, root):
    from itertools import tee
    def dfs(node):
        if node:
            yield from dfs(node.left)
            yield node
            yield from dfs(node.right)

    a, b = tee(dfs(root))
    ans = next(b, None)
    for f, s in zip(a, b):
        f.right = s
        s.left = f
    return ans
```

<font color=#32CD32 size=3>方法二：分别递归处理左子树和右子树。</font>

```python
def Convert(self, root):
    
    def convert_tree(node):
        if not node:
            return None  
        if node.left:
            left = convert_tree(node.left)
            while left.right:
                left = left.right
            left.right = node
            node.left = left
        if node.right:
            right = convert_tree(node.right)
            while right.left:
                right = right.left
            right.left = node
            node.right = right
        return node

    if not root:
        return root
    root = convert_tree(root)
    while root.left:
        root = root.left
    return root
```

<font color=#32CD32 size=3>方法三：Morris Traversal.</font>

```python
def Convert(self, root):
    cur = root
    pre = ans = None
    while cur:
        while cur.left:
            q = cur.left
            while q.right:
                q = q.right
            q.right = cur                   # 补齐右指针
            cur.left, cur = None, cur.left  # 拆掉左指针
        cur.left = pre
        if pre is None:
            ans = cur   # 这里是为了找到链表的头，只执行一次
        else:
            pre.right = cur
        pre, cur = cur, cur.right
    return ans
```
### 37 序列化二叉树

#### [LeetCode传送门](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/)

```python
class Codec:

    def serialize(self, root):
        if not root:
            return '$'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, data):
        
        def deserialize_tree(nodes):
            val = next(nodes)
            if val == '$':
                return None
            root = TreeNode(val)
            root.left = deserialize_tree(nodes)
            root.right = deserialize_tree(nodes)
            return root     
        nodes = iter(data.split(','))
        return deserialize_tree(nodes)
```

### 38 字符串的排列

#### [LeetCode传送门](https://leetcode.com/problems/permutations/description/)这是一道类似的题，求的是数组的全排列，不过在Python中都一样，都是可迭代对象。

使用itertools

```python
def Permutation(self, ss):
    # write code here
    from itertools import permutations
    if not ss:
        return []
    return sorted(list(set([''.join(x) for x in permutations(ss)])))
```
这里注意几点：
 * 为什么要判断`if not ss`，是因为如果`ss=''`的时时候，返回了`['']`而不是`[]`。因为这里返回了一个空的`tuple`，所以在列表推导式中是有一个元素的。

    ```shell
    >>> list(permutations('', 0))
    [()]
    ```
 * 为什么使用`set`去重，因为当`ss='aa'`的时候，牛客网的测试用例要求返回一个元素，即`['aa']`。
 * 排序也是为了满足测试用例。

自己实现。这里拆成两个方法的原因还是因为`ss=''`的时候会影响递归循环。

```python
def Permutation(self, ss):
    if not ss:
        return []
    return self.permute(ss)

def permute(self, ss):
    return sorted(list(set([h + p
        for i, h in enumerate(ss)
        for p in self.permute(ss[:i]+ss[i+1:])
    ]))) or [""]
```

<font color=#32CD32 size=3>方法二：迭代。</font>

```python
def Permutation(self, ss):
    ans = ['']
    for s in ss:
        ans = [p[:i] + s + p[i:]
               for p in ans for i in range((p+s).index(s)+1)]
    return sorted(ans) if ss else []
```


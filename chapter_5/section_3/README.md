### 49 丑数

#### [LeetCode传送门](https://leetcode.com/problems/ugly-number-ii/)

```python
def nthUglyNumber(self, n: int) -> int:
    q = [1]
    t2 = t3 = t5 = 0
    for _ in range(n-1):
        a2, a3, a5 = q[t2]*2, q[t3]*3, q[t5]*5
        to_add = min(a2, a3, a5)
        q.append(to_add)
        if a2 == to_add:
            t2 += 1
        if a3 == to_add:
            t3 += 1
        if a5 == to_add:
            t5 += 1
    return q[-1]
```

### 50 第一个只出现一次的字符

#### [LeetCode传送门](https://leetcode.com/problems/first-unique-character-in-a-string/description/)有一点小区别，LeetCode输出索引，书中输出值。

```
s = "leetcode"
return 0.
s = "loveleetcode",
return 2.
```

Time-O(N), Space-O(N)。暂时没发现更快的算法了。

```python
def firstUniqChar(self, s):
    from collections import Counter
    c = Counter(s)
    for i, ch in enumerate(s):
        if c[ch] == 1:
            return i
    return -1
```

### 51 数组中的逆序对

#### [牛客网传送门](https://www.nowcoder.com/practice/96bd6684e04a44eb80e6a68efc0ec6c5?tpId=13&tqId=11188&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)

#### [AcWing传送门](https://www.acwing.com/problem/content/61/)

这里使用了双端队列感觉不太合适，因为还要显式地转成list，否则没法对剩余的left或right做切片。也试了将其改为stack，但是stack来回reverse又太麻烦。

```python
def InversePairs(self, data):
    self.count = 0
    
    def merge(left, right):
        q = deque()
        l, r = len(left)-1, len(right)-1
        while l >= 0 and r >= 0:
            if left[l] > right[r]:
                self.count += r + 1
                q.appendleft(left[l])
                l -= 1
            else:
                q.appendleft(right[r])
                r -= 1
        # q.extendleft(left[l:-1:-1] or right[r:-1:-1])
        q = left[:l+1] + right[:r+1] + list(q)
        return q
        
    def merge_sort(ary):
        if len(ary) <= 1: return ary
        mid = len(ary) // 2
        left = merge_sort(ary[:mid])
        right = merge_sort(ary[mid:])
        return merge(left, right)
    
    merge_sort(data)
    return self.count % 1000000007
```
### 52 两个链表的第一个公共节点

#### [LeetCode传送门](https://leetcode.com/problems/intersection-of-two-linked-lists/description/)

```python
def getIntersectionNode(self, headA, headB):
    p1, p2 = headA, headB
    while p1 is not p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA
    return p1
```
### 16 数值的整数次方
```python
class Solution(object):

    def myPow(self, x, n):
        if n < 0:
            return 1 / self.pow_with_unsigned(x, -n)
        else:
            return self.pow_with_unsigned(x, n)
              
    def pow_with_unsigned(self, x, n):
        if n == 1:
            return x
        if n == 0:
            return 1
        
        res = self.pow_with_unsigned(x, n >> 1)
        res *= res    
        if n & 1 == 1:
            res *= x
        return res
```

### 18 删除链表中的节点
开始看到这题的思路是，要是能拿到父节点就好了，然后这道题需要别的思路，其关键在于复制
```python
def deleteNode(self, node):
    node.val = node.next.val  # 4->1->1->9
    node.next = node.next.next  # 4->1->9
```

### 19 正则表达式

#### [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/description/)

* 先考虑没有`*`的情况，通过一个递归逐个字符判断

    ```python
    def match(text, pattern):
        if not pattern: return not text
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        return first_match and match(text[1:], pattern[1:])
    ```

* 当`*`出现时，一定会在前面跟一个其他字符，所以一定会出现在pattern[1]的位置。一种情况是我们忽略这对pattern，因为可以出现0次；另一种情况是匹配上这个字符，用递归的方式匹配下一个。

* 一定要用f_match = bool(s)，否则结果可能输出`''`

    ```python
    def match(self, s, pattern):
        if not pattern: return not s
        f_match = bool(s) and pattern[0] in {s[0], '.'}
        if len(pattern) > 1 and pattern[1] == '*':
            return (self.match(s, pattern[2:]) or
                    (f_match and self.match(s[1:], pattern)))
        else:
            return f_match and self.match(s[1:], pattern[1:])
    ```

### 20 表示数值的字符串

#### [65. Valid Number](https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA)

此处留坑，[排名第一的python答案](https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA)暂时没有理解。

### 21 调整数组顺序使奇数位于偶数前面

时间：O(n), 空间O(1)

```python
def reOrderArray(self, array):
    # write code here
    l, r = 0, len(array)-1
    while l < r:
        while l < r and array[l]&1 == 1:
            l += 1
        while l < r and array[r]&1 == 0:
            r -= 1
        array[l], array[r] = array[r], array[l]
```

看了一下没有通过牛客网的测试用例，因为题目有些不同，牛客网要求奇数和奇数，偶数和偶数之前的相对位置不变。

```python
def reOrderArray(array):
    return sorted(array, key=lambda x:x&1==0)
```

不使用sort

```python
def reOrderArray(self, array):
    # write code here
    from collections import deque
    q = deque()
    n = len(array)
    for i in range(n):
        if array[-i-1] & 1 == 1:  # 从后找奇数
            q.appendleft(array[-i-1])
        if array[i] & 1 == 0:  #从前找偶数
            q.append(array[i])
    return q
```
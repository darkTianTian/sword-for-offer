### 10 斐波那契数列

#### [LeetCode传送门](https://leetcode.com/problems/fibonacci-number/)

```python
def fibonacci(n):
    a = b = 1
    for _ in range(n-1):
        a, b = b, a+b
    return b
```

### 11 旋转数组的最小数字

#### [LeetCode传送门](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

说明：通过一个递增数组旋转后的数组，找出最小元素。

思路：通过二分法不断缩小范围，由于mid是整除，最后l==mid，并且nums[mid] > nums[r]的。
```python
def find_min(nums):
    l, r = 0, len(nums)-1
    if nums[l] < nums[r]:
        return nums[l]
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] > nums[l]:
            l = mid
        elif nums[mid] < nums[r]:
            r = mid
        else:
            return nums[r]
```

### 12 矩阵中的路径

#### [LeetCode传送门](https://leetcode.com/problems/word-search/)

**这道题一定一定要去LeetCode上做，牛客网和AcWing的TestCase都差了太多，毫不夸张地说牛客网此题Python排行榜中的答案很多都是错误的**。我写了一篇关于此题的博客，讲述了如何逐步地将一开始的错误代码改正确。这也是一开始我为什么要强调同样的题，要去LeetCode做的原因。[矩阵中的路径，你真的写对了么？](https://darktiantian.github.io/%E7%9F%A9%E9%98%B5%E4%B8%AD%E5%8D%95%E8%AF%8D%E7%9A%84%E8%B7%AF%E5%BE%84%EF%BC%8C%E5%BE%88%E5%A4%9A%E4%BA%BA%E9%83%BD%E9%94%99%E4%BA%86/)

```python
def exist(self, g: List[List[str]], word: str) -> bool:
    R, C = len(g), len(g[0])

    def spread(i, j, w):
        if not w:
            return True
        original, g[i][j] = g[i][j], '-'
        spreaded = False
        for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if (0<=x<R and 0<=y<C and w[0]==g[x][y]
                    and spread(x, y, w[1:])):
                spreaded = True
                break
        g[i][j] = original
        return spreaded

    for i in range(R):
        for j in range(C):
            if g[i][j] == word[0] and spread(i, j, word[1:]):
                return True
    return False
```
### 13 机器人的运动范围

#### [牛客网传送门](https://www.nowcoder.com/practice/6e5207314b5241fb83f2329e89fdecc8?tpId=13&tqId=11219&tPage=4&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)

注意：visited是一维数组。

```python
def movingCount(self, threshold, rows, cols):
    visited = [[False]*cols for _ in range(rows)]
    def get_sum(x, y):
        return sum(map(int, str(x)+str(y)))

    def movingCore(threshold, rows, cols, i, j):
        if get_sum(i, j) <= threshold:
            visited[i][j] = True
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0<=x<rows and 0<=y<cols and not visited[x][y]:
                    movingCore(threshold, rows, cols, x, y)

    movingCore(threshold, rows, cols, 0, 0)
    return sum(sum(visited, []))
```

### 14 剪绳子

#### [AcWing传送门](https://www.acwing.com/problem/content/24/)

说明：数学思想，当`n>=5`时，`2(n-2)>n`并且`3(n-3)>n`，而且`3(n-3) >= 2(n-2)`，所以尽可能多剪长度为3的绳子。如果长度为4的时候，`2*2>3*1`，所以4的时候就剪成`2*2`的两段。

```python
def cut_rope(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    
    # 尽可能剪出3
    timesOf3 = length // 3
    # 如果最后余1，则留一段4分成两半
    if length-timesOf3*3 == 1:
        timeOf3 -= 1
    timesOf2 = (length-timesOf3*3) // 2
    return (3**timesOf3) * (2**timesOf2)
```

### 15 二进制中1的个数

#### [LeetCode传送门](https://leetcode.com/problems/number-of-1-bits/description/)

方法一：常规解法，使用1与n作与运算，如果不是0说明，含有一个1。
```python
def hamming_weight(n):
    count = 0
    for _ in range(32):
        count += (n&1==1)
        n >>= 1
    return count
```
方法二：关键点是，一个数n和n-1的与运算操作，相当于去掉了最右面的1。
```python
def hamming_weigth(n):
    bits = 0
    while n:
        bits += 1
        n = (n-1) & n
    return bits
```
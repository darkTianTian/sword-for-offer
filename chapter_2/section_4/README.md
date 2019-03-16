### 10 斐波那契数列

#### [LeetCode传送门](https://leetcode.com/problems/climbing-stairs/description/)

说明：爬楼梯问题的抽象
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

#### [牛客网传送门](https://www.nowcoder.com/practice/c61c6999eecb4b8f88a98f66b273a3cc?tpId=13&tqId=11218&tPage=4&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)

说明：回溯法。这道题在牛客网上做的，参考了排行前几的答案，却发现了问题，前几的答案中，find方法中的循环都在条件中直接return，这样依赖于整个条件判断的顺序，奇怪的是这样居然可以通过测试用例，可见牛客网的权威性还是不如LeetCode。例如输入`matrix = 'ABEESFCSADME', rows=3, cols=4, path='SEE'`返回了False，实际应该返回True。正确的做法不应直接return，而是保存结果用or判断，判断中也不应该使用`elif`。已经向牛客网多次反馈该问题，却得不到解决。

```python
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols + j] == path[0]:
                    if self.spread(list(matrix), rows, cols, path[1:], i, j):
                        return True
        return False

    def spread(self, matrix, rows, cols, path, i, j):
        if not path:
            return True
        matrix[i*cols + j] = '-'
        spreaded = False
        for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if 0<=x<rows and 0<=y<cols and matrix[x*cols+y]==path[0]:
                if self.spread(matrix, rows, cols, path[1:], x, y):
                    spreaded = True
        return spreaded
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

#### 404.

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
### 39 数组中出现次数超过一半的数字

#### [LeetCode传送门](https://leetcode.com/problems/majority-element/description/)

方法一：排序. Time-O(nlogn), Space-O(n)

```python
def majority_element(nums):
    return sorted(nums)[len(nums)//2]
```

方法二：Counter Time-O(n), Space-O(n)

```python
def majority_element(nums):
    from collections import Counter
    c = Counter(nums)
    # return max(c.keys(), key=c.get)
    return c.most_common(1)[0][0]  
```

<font color=#32CD32 size=3>方法三：Boyer-Moore Voting Algorithm. 书中的算法说的就是这个，这详情请看[波义尔摩尔投票](https://darktiantian.github.io/%E6%B3%A2%E4%B9%89%E5%B0%94%E6%91%A9%E5%B0%94%E6%8A%95%E7%A5%A8%E7%AE%97%E6%B3%95%EF%BC%88Boyer-Moore-Voting-Algorithm%EF%BC%89/)。</font>

```python
def majorityElement(self, nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
```

### 40 最小的k个数

#### 相似题目，但是求最大的k个数[LeetCode传送门](https://leetcode.com/problems/kth-largest-element-in-an-array/)

#### [牛客网传送门](https://www.nowcoder.com/practice/6a296eb82cf844ca8539b57c23e6e9bf?tpId=13&tqId=11182&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tPage=2)

```python
def GetLeastNumbers_Solution(self, tinput, k):
    # write code here
    l, r = 0, len(tinput)-1
    if k > len(tinput) or k < 1: return [] # for passing the damn testcase
    while True:
        pos = self.partition(tinput, l, r)
        if pos < k-1:
            l = pos + 1
        elif pos > k-1:
            r = pos - 1
        else:
            return sorted(tinput[:pos+1])  # sorted for passing the damn testcase
    
def partition(self, nums, l, r):
    from random import randint
    p = randint(l, r)
    nums[r], nums[p] = nums[p], nums[r]
    for i, v in enumerate(nums[l:r+1], l):
        if nums[i] <= nums[r]:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
    return l-1  # the pivot index
```

使用堆，不改变原数组

```python
def GetLeastNumbers_Solution(self, tinput, k):
    import heapq as hq
    if k > len(tinput) or k <= 0: return []
    heap = [-x for x in tinput[:k]]
    hq.heapify(heap)
    for num in tinput[k:]:
        if -heap[0] > num:
            hq.heapreplace(heap, -num)
    return sorted(-x for x in heap)
```

### 41 数据流中的中位数

#### [LeetCode传送门](https://leetcode.com/problems/find-median-from-data-stream/description/)

思路：使用两个堆，最大堆存储较小的数据，最小堆存储较大的数据。添加数字时，先添加到最大堆，然后最大堆返回一个最大的数字给最小堆，最后为了平衡，可能需要最小堆还给最大堆一个最小值，以保证最大堆的长度>=最小堆的长度。由于headpq是最小堆，所以使用取反实现最大堆。添加数字：Time-O(logn)，取出中位数：Time-O(1)。

```python
Adding number 41
MaxHeap lo: [41]           // MaxHeap stores the largest value at the top (index 0)
MinHeap hi: []             // MinHeap stores the smallest value at the top (index 0)
Median is 41
=======================
Adding number 35
MaxHeap lo: [35]
MinHeap hi: [41]
Median is 38
=======================
Adding number 62
MaxHeap lo: [41, 35]
MinHeap hi: [62]
Median is 41
=======================
Adding number 4
MaxHeap lo: [35, 4]
MinHeap hi: [41, 62]
Median is 38
=======================
Adding number 97
MaxHeap lo: [41, 35, 4]
MinHeap hi: [62, 97]
Median is 41
=======================
Adding number 108
MaxHeap lo: [41, 35, 4]
MinHeap hi: [62, 97, 108]
Median is 51.5
```
```python
import heapq as hq

class MedianFinder:

    def __init__(self):
        self.lo, self.hi = [], []  # lo is max_heap, hi is min_heap
        
    def addNum(self, num):
        hq.heappush(self.lo, -num)
        hq.heappush(self.hi, -hq.heappop(self.lo))
        
        if len(self.lo) < len(self.hi):
            hq.heappush(self.lo, -hq.heappop(self.hi))       

    def findMedian(self):
        if len(self.lo) == len(self.hi):
            return (-self.lo[0]+self.hi[0]) / 2.0
        else:
            return float(-self.lo[0])
```

### 42 连续子数组的最大和

#### [LeetCode传送门](https://leetcode.com/problems/maximum-subarray/description/)

方法一：书中的思想。

```python
def maxSubArray(self, nums):
    cp_nums = nums[:]
    for i in range(1, len(nums)):
        if cp_nums[i-1] > 0:
            cp_nums[i] += cp_nums[i-1]
    return max(cp_nums)
```

方法二：one-liner。注意`accumulate`是把函数放到后面的。

```python
def maxSubArray(self, nums):
    from itertools import accumulate
    return max(accumulate(nums, lambda x, y: x+y if x > 0 else y))
```

### 43 1~n整数中1出现的次数

#### [LeetCode传送门](https://leetcode.com/problems/number-of-digit-one/description/)

```python
def countDigitOne(self, n):    
    countr, i = 0, 1
    while i <= n:
        divider = i * 10
        countr += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
        i *= 10
    return countr
```

### 44 数字序列中某一位的数字

#### [LeetCode传送门](https://leetcode.com/problems/nth-digit/)

```python
def findNthDigit(self, n):
    start, step, size = 1, 9, 1
    while n > size * step:
        n, start, step, size = n-size*step, start*10, step*10, size+1
    return int(str(start + (n-1)//size)[(n-1) % size])
```
### 45 把数组排成最小的数字

#### [牛客网传送门](https://www.nowcoder.com/practice/8fecd3f8ba334add803bf2a06af1b993?tpId=13&tqId=11185&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
#### [AcWing传送门](https://www.acwing.com/problem/content/54/)

python2的写法。

```python
def PrintMinNumber(self, numbers):
    return ''.join(sorted(map(str, numbers), 
                          lambda x, y: cmp(x+y, y+x)))
```
匿名函数作为sort的参数，在python2中有这个参数。

> cmp specifies a custom comparison function of two arguments (iterable elements) which should return a negative, zero or positive number depending on whether the first argument is considered smaller than, equal to, or larger than the second argument: cmp=lambda x,y: cmp(x.lower(), y.lower()). The default value is None.

作为sort的参数，cmp提供了一个自定义的比较两个元素的方法，如果返回-1表示前者小于后者。python3中取消了这个参数，但是提供了一种key的转换。而内置函数可以通过运算符实现。

```python
cmp(a, b) 
```
等同于

```python
(a>b) - (a<b)
```

所以python3的写法如下：

```python
from functools import cmp_to_key
def PrintMinNumber(self, numbers):
    nums = list(map(str, numbers))
    nums.sort(key=cmp_to_key(lambda x, y: ((x+y)>(y+x)) - ((y+x)>(x+y))))
    return ''.join(nums)
```

### 46 把数字翻译成字符串

#### [LeetCode传送门](https://leetcode.com/problems/decode-ways/)

```python
def numDecodings(self, s: str) -> int:
    # w tells the number of ways
    # v tells the previous number of ways
    # d is the current digit
    # p is the previous digit
    v, w, p = 0, int(s>''), ''
    for d in s:
        v, w, p = w, int(d>'0')*w + (9<int(p+d)<27)*v, d
    return w
```
### 47 礼物的最大价值

#### [LeetCode传送门](https://leetcode.com/problems/unique-paths/)。相似题目，不过也差不少。

#### [Acwing传送门](https://www.acwing.com/problem/content/56/)这个是原题。

对首行使用初始化，然后消除了i的判断。

```python
def get_max_value(g: 'List[List[int]]') -> int:
    R, C = len(g), len(g[0])
    cur = list(itertools.accumulate(g[0]))
    for i in range(1, R):
        tmp = []
        for j in range(C):
            left = tmp[-1] if j > 0 else float('-inf')
            tmp.append(max(cur[j], left) + g[i][j])
        cur = tmp
    return cur[-1]
```
### 48 最长不含重复字符的子字符串

#### [LeetCode传送门](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

方法二：找到重复值时，更新start的值，为什么使用max，因为start有可能大于`dic[s[end]]+1`，比如当`s='abba'`，end走到最后的时候，上一次start因为b做了更新变为了2。

```python
def lengthOfLongestSubstring(self, s):
    ans = start = 0
    pos = {}    # last index of element
    for end, c in enumerate(s):
        if c in pos:
            start = max(start, pos[c]+1)
        pos[c] = end
        ans = max(ans, end-start+1)
    return ans
```


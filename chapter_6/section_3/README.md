### 53 在排序数组中查找数字

#### [LeetCode传送门](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/)。相似题目，LeetCode要返回两个索引，书中求个数。

```python
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```
方法一：标准库写法。这里不需要target去整个nums中判断。

```python
def searchRange(self, nums: List[int], target: int) -> List[int]:
    from bisect import bisect, bisect_left
    lo = bisect_left(nums, target)
    if target in nums[lo:lo+1]:
        return lo, bisect(nums, target)-1
    else:
        return -1, -1
```
方法二：自己实现。bisect_right的方式采用+1的形式。

```python
def searchRange(self, nums: List[int], target: int) -> List[int]:

    def search(n):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo
    lo = search(target)
    if target in nums[lo:lo+1]:
        return lo, search(target+1)-1
    else:
        return -1, -1
```

### 53 0~n-1中缺失的数字

#### [LeetCode传送门](https://leetcode.com/problems/missing-number/description/)

相似题目，LeetCode是未排序，书中是已排序。所以可以利用排序的特性使时间复杂度小于O(n)。即找出第一个下标与值不相等的元素，再-1就是缺失的元素。

#### [AcWing传送门](https://www.acwing.com/problem/content/64/)

方法一：数学公式。

```python
def missingNumber(self, nums):
    n = len(nums)
    expected_sum = n*(n+1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
```

方法二：XOR.

| index | 0    | 1    | 2    |
| ----- | ---- | ---- | ---- |
| value | 3    | 0    | 1    |

```python
def missingNumber(self, nums: 'List[int]') -> 'int':
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing
```

方法三：利用书中已排序的特性。

```python
def getMissingNumber(self, nums):
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo + hi) >> 1
        if nums[mid] != mid:
            if mid==0 or nums[mid-1]==mid-1:
                return mid
            hi = mid - 1
        else:
            lo = mid + 1
    return lo
```

### 53 数组中数值和下标相等的元素

#### [AcWing传送门](https://www.acwing.com/problem/content/65/)

```python
def getNumberSameAsIndex(self, nums):
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo + hi) >> 1
        if nums[mid] < mid:
            lo = mid + 1
        elif nums[mid] > mid:
            hi = mid - 1
        else:
            return mid
    return -1
```

### 54 二叉搜索树的第k大节点

#### [牛客网传送门](https://www.nowcoder.com/practice/ef068f602dde4d28aab2b210e859150a?tpId=13&tqId=11215&tPage=4&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
#### [AcWing传送门](https://www.acwing.com/problem/content/66/)

注意：牛客网上是求第k小节点，这里被坑了一次，然后返回值居然要求返回节点对象，而不是节点值，这里的答案按书中返回。如果是牛客网上需要把节点添加到`res`中，然后`return res[k-1]`

```python
def kth_largest(self, root: TreeNode, k: int) -> int:
    stack, ans = [], None
    while stack or root:
        while root:
            stack.append(root)
            root = root.right
        root = stack.pop()
        k -= 1
        ans = root
        root = root.left
        if k == 0:
            return ans
```

### 55 二叉树的深度

#### [LeetCode传送门](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)

```
    3
   / \
  9  20
    /  \
   15   7
return 3
```

方法一：recursively

```python
def max_depth(root):
    if not root:
        return 0
    # return max(max_depth(root.left), max_depth(root.right)) + 1
    return max(map(max_depth, (root.left, root.right))) + 1
```

方法二：iteratively. BFS with deque

```python
def maxDepth(self, root: 'TreeNode') -> 'int':
    q = root and collections.deque([(root, 1)])
    d = 0
    while q:
        node, d = q.popleft()
        if node.right:
            q.append((node.right, d+1))
        if node.left:
            q.append((node.left, d+1))
    return d
```

### 55_1 平衡二叉树

#### [LeetCode传送门](https://leetcode.com/problems/balanced-binary-tree/description/)

方法一：递归+递归。

```python
def isBalanced(self, root):
    if not root:
        return True
    return self.isBalanced(root.left) and self.isBalanced(root.right) and \
           abs(self.max_depth(root.left)-self.max_depth(root.right)) <= 1
    
def max_depth(self, root):
    if not root:
        return 0
    return max(self.max_depth(root.left), self.max_depth(root.right)) + 1
```

方法二：上诉两种方法中都包含了一些无意义的重复遍历。这里采用后序遍历，边遍历边判断，不会重复节点。受此思想启发，添加一种后序遍历二叉树的方法。

```python
def isBalanced(self, root):
    stack, node, last = [], root, None
    depths = collections.defaultdict(int)
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            if not node.right or last == node.right:
                node = stack.pop()
                left, right  = depths[node.left], depths[node.right]
                if abs(left - right) > 1: 
                    return False
                depths[node] = 1 + max(left, right)
                last, node = node, None
            else:
                node = node.right
    return True
```

方法三：dfs. 算深度的时候判断左右是否深度超过1. 这里变量不能把self去掉，否则`[1,2,2,3,3,null,null,4,4]`会错误的返回`True`而不是`False`。也可以使用`nonlocal`

```python
def isBalanced(self, root: 'TreeNode') -> 'bool':
    self.balanced = True
    
    def dfs(node):
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        if abs(left-right) > 1 and self.balanced:
            self.balanced = False
        return max(left, right) + 1
    
    dfs(root)
    return self.balanced
```

### 56 数组中只出现一次的两个数字。

#### 找出数组中两个唯一出现一次的元素，其余元素均出现两次。[LeetCode传送门](https://leetcode.com/problems/single-number-iii/description/)

```
Input:  [1,2,1,3,2,5]
Output: [3,5]
```

思想：将这两个元素分到两个组，由于这两个数不相等，所以亦或结果不为0，也就是说二进制中至少有一位1，记为第n位。我们以第n位是否为1，把数组分为两个子数组。

```python
def singleNumber(self, nums: List[int]) -> List[int]:
    from functools import reduce
    def get_single(nums):
        return reduce(operator.xor, nums)
    
    total_xor = get_single(nums)
    mask = 1
    while total_xor&mask == 0:
        mask <<= 1
    n1 = [num for num in nums if num&mask==0]
    n2 = [num for num in nums if num&mask!=0]
    return get_single(n1), get_single(n2)
```

### 56_1 数组中出现一次的数字，其余元素出现三次。

#### [LeetCode传送门](https://leetcode.com/problems/single-number-ii/description/)

```
Input: [2,2,3,2]
Output: 3
```

方法一：找出单独元素每一位的值。如果把所有数字的二进制每一位加起来，如果某一位可以被3整除，则表示单独元素的该位为0，否则为1。以下使用`count`来表示每一位`1`的个数。假设`count%3!=0`为True，说明该元素`i`位为1，然后是用`|=`更新ans在第`i`个位置的值，这里也可以使用`+=`，但是效率稍慢。`convert`的作用是因为python中的int是个对象，且没有最大限制，不是在第32位使用1来表示负数。

```python
def singleNumber(self, nums, n=3):
    ans = 0
    for i in range(32):
        count = 0
        for num in nums:
            if ((num >> i) & 1):
                count += 1
        ans |= ((count%n!=0) << i)
    return self.convert(ans)

def convert(self, x):
    if x >= 2**31:
        x -= 2**32
    return x
```

这里有个状态机的解法，不明觉厉，留坑。[讨论1](https://leetcode.com/problems/single-number-ii/discuss/43294/Challenge-me-thx?page=2)和[讨论2](https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers)

```python
def singleNumber(self, nums):
    ones, twos = 0, 0;
    for i in range(len(nums)):
        ones = (ones ^ nums[i]) & ~twos
        twos = (twos ^ nums[i]) & ~ones
    return ones
```

### 57 和为s的数字
#### [牛客网传送门](https://www.nowcoder.com/practice/390da4f7a00f44bea7c2f3d19491311b?tpId=13&tqId=11195&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
#### [AcWing传送门](https://www.acwing.com/problem/content/71/)

看牛客网上的描述，如果有多对数字和为s，要求返回乘积最小的一对。乍一看以为牛客网又乱改题，但是仔细一想，如果两个和为s的数，而且是在递增数组中很明显，边缘的数字乘积要小，例如`8X8>1X15`。所以还是和书中解法一样。

```python
def FindNumbersWithSum(self, array, tsum):
    l, r = 0, len(array)-1
    while l < r:
        if array[l] + array[r] < tsum:
            l += 1
        elif array[l]+array[r] > tsum:
            r -= 1
        else:
            return array[l], array[r]
    return []
```

### 57_1 和为s的连续正数序列

#### [牛客网传送门](https://www.nowcoder.com/practice/c451a3fd84b64cb19485dad758a55ebe?tpId=13&tqId=11194&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)

#### [AcWing传送门](https://www.acwing.com/problem/content/72/)

```python
def findContinuousSequence(self, tsum):
    end = (tsum + 1) // 2
    lo, hi, cur_sum = 1, 2, 3
    ans = []
    while lo < end:
        if cur_sum < tsum:
            hi += 1
            cur_sum += hi
        else:
            if cur_sum == tsum:
                ans.append(list(range(lo, hi+1)))
            cur_sum -= lo
            lo += 1
    return ans
```

### 58 翻转字符串

#### [LeetCode传送门](https://leetcode.com/problems/reverse-words-in-a-string/description/)

```python
Input: "the sky is blue",
Output: "blue is sky the".
```
方法一：如果面试官是一个Pythoner，那么就让你过了。

```python
def reverse_words(s):
    return ' '.join(reversed(s.split()))
```

如果你的面试官是一个只写Java或者C，看见代码就不平衡了，凭啥可以写到一行，非要你实现reverse。

```python
def reverseWords(self, s: str) -> str:

    def hp_reversed(s):
        s = list(s)
        for i in range(len(s)//2):
            # s[i], s[-i-1] = s[-i-1], s[i]
            s[i], s[~i] = s[~i], s[i]
        return ''.join(s)
    s = hp_reversed(s)
    return ' '.join(hp_reversed(word) for word in s.split())
```

实现`split`，hp_reverse，

```python
def reverseWords(self, s: str) -> str:

    def hp_reversed(s):
        s = list(s)
        for i in range(len(s)//2):
            s[i], s[~i] = s[~i], s[i]
        return ''.join(s)

    s = hp_reversed(s)
    ans = word = ''
    for r, c in enumerate(s):
        if c != ' ':
            word += c
        if (c== ' ' or r==len(s)-1) and word:
            ans += hp_reversed(word) + ' '
            word = ''
    return ans[:-1]
```

### 58_1 左旋转字符串

#### [牛客网传送门](https://www.nowcoder.com/practice/12d959b108cb42b1ab72cef4d36af5ec?tpId=13&tqId=11196&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)
#### [AcWing传送门](https://www.acwing.com/problem/content/74/)

切片，书中的方法个人觉得Python并不适用。

```python
def LeftRotateString(self, s, n):
    if not s:
        return ''
    n = n % len(s)
    return s[n:] + s[:n]
```

### 59 滑动窗口的最大值

#### [牛客网传送门](https://www.nowcoder.com/practice/1624bc35a45c42c0bc17d17fa0cba788?tpId=13&tqId=11217&tPage=4&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
#### [AcWing传送门](https://www.acwing.com/problem/content/75/)

得益于python的切片。Time: O(n*k). k=n-size

```python
def maxInWindows(self, nums, size):
    return [max(nums[i:i+size])
            for i in range(len(nums)-size+1) if size!=0 ]
```

方法二：常规写法，只是将书中的代码封装了一下，Time: O(n). 

```python
def maxInWindows(self, nums, size):
    from collections import deque
    q = deque()
    ans = []
    def pop_less(i):
        # nums[i] 索引和值都比队列尾的元素大，队列尾的元素就没有必要存在了
        while q and nums[i]>=nums[q[-1]]:
            q.pop()
        q.append(i)

    for i in range(size):
        pop_less(i)

    for i in range(size, len(nums)):
        ans.append(nums[q[0]])
        pop_less(i)
        while q and q[0]<= i-size:
            q.popleft()
    ans.append(nums[q[0]])
    return ans   
```
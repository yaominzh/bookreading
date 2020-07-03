[[TOC]]

# 00 学习算法和刷题的框架思维
[00 学习算法和刷题的框架思维](https://labuladong.gitbook.io/algo/di-ling-zhang-bi-du-xi-lie)
## 一、数据结构的存储方式

数据结构的存储方式只有两种：数组（顺序存储）和链表（链式存储）。
## 二、数据结构的基本操作
任何数据结构，其基本操作无非遍历 + 访问，再具体一点就是：增删查改

线性就是 for/while 迭代为代表，非线性就是递归为代表
数组遍历框架，典型的线性迭代结构
```java
void traverse(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        // 迭代访问 arr[i]
    }
}
```
链表遍历框架，兼具迭代和递归结构：
```java
/* 基本的单链表节点 */
class ListNode {
    int val;
    ListNode next;
}

void traverse(ListNode head) {
    for (ListNode p = head; p != null; p = p.next) {
        // 迭代访问 p.val
    }
}

void traverse(ListNode head) {
    // 递归访问 head.val
    traverse(head.next)
}
```
二叉树遍历框架，典型的非线性递归遍历结构：
```java
/* 基本的二叉树节点 */
class TreeNode {
    int val;
    TreeNode left, right;
}

void traverse(TreeNode root) {
    traverse(root.left)
    traverse(root.right)
}
```
二叉树框架可以扩展为 N 叉树的遍历框架：
```java
/* 基本的 N 叉树节点 */
class TreeNode {
    int val;
    TreeNode[] children;
}

void traverse(TreeNode root) {
    for (TreeNode child : root.children)
        traverse(child);
}
```
## 三、算法刷题指南

数据结构是工具，算法是通过合适的工具解决特定问题的方法
先刷二叉树，先刷二叉树，先刷二叉树！
因为二叉树是最容易培养框架思维的，而且大部分算法技巧，本质上都是树的遍历问题。
```java
void traverse(TreeNode root) {
    // 前序遍历
    traverse(root.left)
    // 中序遍历
    traverse(root.right)
    // 后序遍历
}
```
回溯算法就是个 N 叉树的前后序遍历问题，没有例外。

# 01 学习数据结构和算法读什么书
《算法4》看起来挺厚的，但是前面几十页是教你 Java 的；每章后面还有习题，占了不少页数；每章还有一些数学证明，这些都可以忽略。这样算下来，剩下的就是基础知识和疑难解答之类的内容，含金量很高，把这些基础知识动手实践一遍，真的就可以达到不错的水平了

学习就要带着目的性去学，大部分人学算法不就是巩固计算机知识，对付面试题目吗？如果是这个目的，那就学些基本的数据结构和经典算法，明白它们的时间复杂度，然后去刷题就好了，何必和习题、证明过不去？

# 02 推荐极客时间的算法+MySQL
算法这个东西的重要性都是炒作出来的，因为现在做技术的竞争大，大厂也就只能拿算法题筛选一下了。但是实际工作中，我们刷的算法题还真没太大用处，而学好一些通用的计算机技术是非常重要的

再强调一遍，刷题的关键不在多，也不在难，而在于运用

# 03 动态规划解题套路框架
首先，动态规划问题的一般形式就是求最值。动态规划其实是运筹学的一种最优化方法，只不过在计算机问题上应用比较多，比如说让你求最长递增子序列呀，最小编辑距离呀等等

求最值，[核心问题]是什么呢？求解动态规划的核心问题是穷举. 因为要求最值，肯定要把所有可行的答案穷举出来，然后在其中找最值呗。

[动态规划三要素]重叠子问题、最优子结构、状态转移方程

框架

明确 base case -> 明确「状态」-> 明确「选择」 -> 定义 dp 数组/函数的含义。
## 一、斐波那契数列
1、暴力递归
```cpp
int fib(int N) {
    if (N == 1 || N == 2) return 1;
    return fib(N - 1) + fib(N - 2);
}
```
2、带备忘录的递归解法
```cpp
int fib(int N) {
    if (N < 1) return 0;
    // 备忘录全初始化为 0
    vector<int> memo(N + 1, 0);
    // 进行带备忘录的递归
    return helper(memo, N);
}

int helper(vector<int>& memo, int n) {
    // base case 
    if (n == 1 || n == 2) return 1;
    // 已经计算过
    if (memo[n] != 0) return memo[n];
    memo[n] = helper(memo, n - 1) + helper(memo, n - 2);
    return memo[n];
}
```
3、dp 数组的迭代解法
千万不要看不起暴力解，动态规划问题最困难的就是写出这个暴力解，即状态转移方程
```cpp
int fib(int N) {
    vector<int> dp(N + 1, 0);
    // base case
    dp[1] = dp[2] = 1;
    for (int i = 3; i <= N; i++)
        dp[i] = dp[i - 1] + dp[i - 2];
    return dp[N];
}
```
4、状态压缩
如果我们发现每次状态转移只需要 DP table 中的一部分，那么可以尝试用状态压缩来缩小 DP table 的大小，只记录必要的数据
```cpp
int fib(int n) {
    if (n == 2 || n == 1) 
        return 1;
    int prev = 1, curr = 1;
    for (int i = 3; i <= n; i++) {
        int sum = prev + curr;
        prev = curr;
        curr = sum;
    }
    return curr;
}
```

## 二、凑零钱问题
题目：给你 k 种面值的硬币，面值分别为 c1, c2 ... ck，每种硬币的数量无限，再给一个总金额 amount，问你最少需要几枚硬币凑出这个金额，如果不可能凑出，算法返回 -1
1、暴力递归

如何列出正确的状态转移方程？
```cpp
def coinChange(coins: List[int], amount: int):

    def dp(n):
        # base case
        if n == 0: return 0
        if n < 0: return -1
        # 求最小值，所以初始化为正无穷
        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            # 子问题无解，跳过
            if subproblem == -1: continue
            res = min(res, 1 + subproblem)

        return res if res != float('INF') else -1

    return dp(amount)
```
2、带备忘录的递归
```python
def coinChange(coins: List[int], amount: int):
    # 备忘录
    memo = dict()
    def dp(n):
        # 查备忘录，避免重复计算
        if n in memo: return memo[n]
        # base case
        if n == 0: return 0
        if n < 0: return -1
        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1: continue
            res = min(res, 1 + subproblem)

        # 记入备忘录
        memo[n] = res if res != float('INF') else -1
        return memo[n]

    return dp(amount)
```
3、dp 数组的迭代解法
```cpp
int coinChange(vector<int>& coins, int amount) {
    // 数组大小为 amount + 1，初始值也为 amount + 1
    vector<int> dp(amount + 1, amount + 1);
    // base case
    dp[0] = 0;
    // 外层 for 循环在遍历所有状态的所有取值
    for (int i = 0; i < dp.size(); i++) {
        // 内层 for 循环在求所有选择的最小值
        for (int coin : coins) {
            // 子问题无解，跳过
            if (i - coin < 0) continue;
            dp[i] = min(dp[i], 1 + dp[i - coin]);
        }
    }
    return (dp[amount] == amount + 1) ? -1 : dp[amount];
}
```
计算机解决问题其实没有任何奇技淫巧，它唯一的解决办法就是穷举，穷举所有可能性。算法设计无非就是先思考“如何穷举”，然后再追求“如何聪明地穷举”。

备忘录、DP table 就是在追求“如何聪明地穷举”。用空间换时间的思路，是降低时间复杂度的不二法门


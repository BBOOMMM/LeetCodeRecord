#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=30204
#
# [322] 零钱兑换
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i][j] 表示使用前 i 个硬币，组成金额 j 的最少硬币数量
        n = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j < coins[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)
        return dp[n][amount] if dp[n][amount] != float('inf') else -1
# @lc code=end



#
# @lcpr case=start
# [1, 2, 5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#


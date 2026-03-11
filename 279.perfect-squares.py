#
# @lc app=leetcode.cn id=279 lang=python3
# @lcpr version=30204
#
# [279] 完全平方数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import math

class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] 表示和为i的平方数最少数量
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, int(math.sqrt(i))+1):
                dp[i] = min(dp[i], 1+dp[i - j*j])
        return dp[n]
# @lc code=end



#
# @lcpr case=start
# 12\n
# @lcpr case=end

# @lcpr case=start
# 13\n
# @lcpr case=end

#


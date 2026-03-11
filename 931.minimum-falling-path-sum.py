#
# @lc app=leetcode.cn id=931 lang=python3
# @lcpr version=30204
#
# [931] 下降路径最小和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp[i][j] 为到达 matrix[i][j] 的最小路径和
        m = len(matrix)
        n = len(matrix[0])
        dp = [[float('inf')]*n for _ in range(m)]
        
        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = min(dp[i][j], matrix[i][j] + dp[i-1][j])
                if j>0:
                    dp[i][j] = min(dp[i][j], matrix[i][j] + dp[i-1][j-1])
                if j<n-1:
                    dp[i][j] = min(dp[i][j], matrix[i][j] + dp[i-1][j+1])
        
        return min(dp[m-1][:])
# @lc code=end



#
# @lcpr case=start
# [[2,1,3],[6,5,4],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[-19,57],[-40,-5]]\n
# @lcpr case=end

#


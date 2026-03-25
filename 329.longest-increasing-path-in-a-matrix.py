#
# @lc app=leetcode.cn id=329 lang=python3
# @lcpr version=30204
#
# [329] 矩阵中的最长递增路径
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def dfs(self, i, j, m, n, matrix, dp):
        if i<0 or i>=m or j<0 or j>=n:
            return 0
        # 上下左右，返回的是以下一个为起点的最长递增长度
        # 上
        up = 0
        if i-1>=0 and matrix[i-1][j] > matrix[i][j]:
            if dp[i-1][j] > 0:
                up = dp[i-1][j]
            else:
                up = self.dfs(i-1, j, m, n, matrix, dp)
        # 下
        down = 0
        if i+1 < m and matrix[i+1][j] > matrix[i][j]:
            if dp[i+1][j] > 0:
                down = dp[i+1][j]
            else:
                down = self.dfs(i+1, j, m, n, matrix, dp)
        # 左
        left = 0
        if j-1 >= 0 and matrix[i][j-1] > matrix[i][j]:
            if dp[i][j-1] > 0:
                left = dp[i][j-1]
            else:
                left = self.dfs(i, j-1, m, n, matrix, dp)
        # 右
        right = 0
        if j+1 < n and matrix[i][j+1] > matrix[i][j]:
            if dp[i][j+1] > 0:
                right = dp[i][j+1]
            else:
                right = self.dfs(i, j+1, m, n, matrix, dp)
        
        dp[i][j] = 1 + max(up, down, left, right)
        return dp[i][j]
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[float('-inf')] * n for _ in range(m)]
        ans = float('-inf')
        for i in range(m):
            for j in range(n):
                if dp[i][j] > 0:
                    ans = max(ans, dp[i][j])
                else:
                    self.dfs(i, j, m, n, matrix, dp)
                    ans = max(ans, dp[i][j])
        return ans
# @lc code=end



#
# @lcpr case=start
# [[9,9,4],[6,6,8],[2,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,4,5],[3,2,6],[2,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1]]\n
# @lcpr case=end

#


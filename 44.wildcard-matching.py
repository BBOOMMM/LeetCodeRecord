#
# @lc app=leetcode.cn id=44 lang=python3
# @lcpr version=30204
#
# [44] 通配符匹配
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [ [False] * (n+1) for _ in range(m+1) ]
        dp[0][0] = True
        for j in range(n):
            if p[j] == '*':
                dp[0][j+1] = True 
            else:
                break
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    # 用*号  dp[i-1][j]
                    # 不用*号  dp[i][j-1]
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif p[j-1] == '?':
                    if dp[i-1][j-1]:
                        dp[i][j] = True
                else:
                    if p[j-1] == s[i-1] and dp[i-1][j-1]:
                        dp[i][j] = True
        # for i in range(m+1):
        #     print(dp[i])
        return dp[m][n]
# @lc code=end



#
# @lcpr case=start
# "aa"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"*"\n
# @lcpr case=end

# @lcpr case=start
# "cb"\n"?a"\n
# @lcpr case=end

#


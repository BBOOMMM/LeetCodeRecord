#
# @lc app=leetcode.cn id=416 lang=python3
# @lcpr version=30204
#
# [416] 分割等和子集
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        # dp[i][j] 表示前 i 个物品在容量为 j 的背包中能获得的最大价值
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        for i in range(1, n+1):
            for j in range(1, target+1):
                dp[i][j] = dp[i-1][j]
                if j - nums[i-1] >= 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-nums[i-1]] + nums[i-1])
        if dp[n][target] == target:
            return True
        return False
# @lc code=end



#
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#


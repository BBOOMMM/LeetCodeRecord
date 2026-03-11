#
# @lc app=leetcode.cn id=1262 lang=python3
# @lcpr version=30204
#
# [1262] 可被三整除的最大和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # dp[i] 表示前 i 个数字，能被 3 整除的最大元素和
        n = len(nums)
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = dp[i-1]
            for j in range(i):
                if (nums[i-1] + dp[j]) % 3==0: 
                    dp[i] = max(dp[i], nums[i-1] + dp[j])
        return dp[n]
# @lc code=end



#
# @lcpr case=start
# [3,6,5,1,8]\n
# @lcpr case=end

# @lcpr case=start
# [4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,4]\n
# @lcpr case=end

#


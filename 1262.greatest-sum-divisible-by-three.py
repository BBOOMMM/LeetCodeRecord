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
        # n = len(nums)
        # dp = [0] * (n+1)
        # for i in range(1, n+1):
        #     dp[i] = dp[i-1]
        #     for j in range(i):
        #         if (nums[i-1] + dp[j]) % 3==0: 
        #             dp[i] = max(dp[i], nums[i-1] + dp[j])
        # 这样错误，因为dp[j]一定能被3整除，nums[i-1] + dp[j]能被3整除直接变成了nums[i-1]能被3整除，所以要记录模的所有状态
        
        n = len(nums)
        # dp[i][j] 表示前 i 个数字，能被 3 整除余 j 的最大元素和
        dp = [[0]*3 for _ in range(n+1)]
        # 这边初始化很重要
        dp[0][1] = float('-inf')
        dp[0][2] = float('-inf') 
        for i in range(1, n+1):
            mod = nums[i-1] % 3
            # 用这个数字
            if mod == 0:
                dp[i][0] = max(dp[i-1][0], dp[i-1][0]+nums[i-1])
                dp[i][1] = max(dp[i-1][1], dp[i-1][1]+nums[i-1])
                dp[i][2] = max(dp[i-1][2], dp[i-1][2]+nums[i-1])
            elif mod == 1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][2]+nums[i-1])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]+nums[i-1])
                dp[i][2] = max(dp[i-1][2], dp[i-1][1]+nums[i-1])
            elif mod == 2:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+nums[i-1])
                dp[i][1] = max(dp[i-1][1], dp[i-1][2]+nums[i-1])
                dp[i][2] = max(dp[i-1][2], dp[i-1][0]+nums[i-1])
        # for i in range(n+1):
            # print(dp[i])
        return dp[n][0]
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


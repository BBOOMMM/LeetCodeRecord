#
# @lc app=leetcode.cn id=813 lang=python3
# @lcpr version=30204
#
# [813] 最大平均值和的分组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # 首先平均值和最大一定要分 k 组，可以用反证法证明
        # dp[i][j] 表示 nums 前 i 个数字，分成 j 组的最大平均值和
        n = len(nums)
        dp = [ [0]*(k+1) for _ in range(n+1) ]
        # dp[0][j] = 0
        # dp[i][0] = 0
        # dp[i][j] = max( dp[i-k][j-1] + average(nums[i-k : i]) )
        presum = [0] * n 
        presum[0] = nums[0]
        for i in range(1, n):
            presum[i] = presum[i-1] + nums[i]
        for i in range(1, n+1):
            for j in range(1, k+1):
                if j==1:
                    dp[i][j] = presum[i-1] / float(i)
                else:       
                    for p in range(1, i+1):
                        if i-p < j-1:
                            continue
                        # 当前组是 nums[i-p : i-1]
                        cur_avg = (presum[i-1] - presum[i-p-1]) / float(p)
                        # 前面剩余的是 dp[i-k][j-1]
                        # i - k 必须大于等于 j-1，才能分成j-1组合
                        dp[i][j] = max(dp[i][j], dp[i-p][j-1] + cur_avg)
        for d in dp:
            print(d)
        return dp[n][k]
# @lc code=end



#
# @lcpr case=start
# [9,1,2,3,9]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7]\n4\n
# @lcpr case=end

#


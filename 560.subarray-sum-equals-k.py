#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30204
#
# [560] 和为 K 的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = 0
        d = {0:1}
        ans = 0
        for i in range(len(nums)):
            num = nums[i]
            presum += num
            to_find = presum - k
            ans += d.get(to_find, 0)
            d[presum] = d.get(presum, 0) + 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30204
#
# [209] 长度最小的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 双指针动态范围
        low = 0
        quick = 0
        n = len(nums)
        min_len = float('inf')
        cur_sum = 0
        while quick < n:
            cur_sum += nums[quick]
            if cur_sum >= target:
                while cur_sum >= target:
                    cur_len = quick - low + 1
                    if cur_len < min_len:
                        min_len = cur_len
                    # 现在已经满足，如果更后面的需要用到更前面的，这个长度一定比现在长
                    cur_sum -= nums[low]
                    low += 1
            quick += 1
        if min_len <= n:
            return min_len
        return 0
# @lc code=end



#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#


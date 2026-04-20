#
# @lc app=leetcode.cn id=128 lang=python3
# @lcpr version=30204
#
# [128] 最长连续序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0
        while s:
            num = s.pop()
            cur_len = 1
            up = num + 1
            while up in s:
                s.remove(up)
                up += 1
                cur_len += 1
            low = num - 1
            while low in s:
                s.remove(low)
                low -= 1
                cur_len += 1
            max_len = max(max_len, cur_len)
        return max_len
# @lc code=end



#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,2]\n
# @lcpr case=end

#


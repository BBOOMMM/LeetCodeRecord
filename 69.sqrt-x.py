#
# @lc app=leetcode.cn id=69 lang=python3
# @lcpr version=30204
#
# [69] x 的平方根 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        mid = None
        while left <= right:
            mid = (left + right) // 2
            cur = mid * mid
            if cur == x:
                return mid
            elif cur > x:
                right = mid - 1
            else:
                left = mid + 1
        return right
# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 8\n
# @lcpr case=end

#


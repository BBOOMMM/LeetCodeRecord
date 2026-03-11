#
# @lc app=leetcode.cn id=7 lang=python3
# @lcpr version=30204
#
# [7] 整数反转
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        boundary = None
        sign = 1
        if x < 0:
            boundary = 1<<31
            sign = -1
            x=-x
        else:
            boundary = (1<<31) - 1
            # 要加括号，因为减法的优先级更高
        res = 0
        while x != 0:
            cur = x % 10
            res = res * 10 + cur
            x = x // 10
        #     print(res)
        # print(boundary)
        if res > boundary:
            return 0
        return res*sign
# @lc code=end



#
# @lcpr case=start
# 123\n
# @lcpr case=end

# @lcpr case=start
# -123\n
# @lcpr case=end

# @lcpr case=start
# 120\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

#


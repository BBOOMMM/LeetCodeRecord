#
# @lc app=leetcode.cn id=470 lang=python3
# @lcpr version=30204
#
# [470] 用 Rand7() 实现 Rand10()
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            a, b = rand7(), rand7()
            cur = (a - 1) + 7 * (b-1) + 1 # [1, 49]
            if cur <= 40:
                return (cur % 10) + 1
# @lc code=end



#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#


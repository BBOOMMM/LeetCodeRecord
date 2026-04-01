#
# @lc app=leetcode.cn id=227 lang=python3
# @lcpr version=30204
#
# [227] 基本计算器 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        ops = []
        nums = []
        for i in range(len(s)):
            if s[i] == '+' or s[i] == '-':
                ops.append(s[i])
            elif s[i] == '*' or s[i] == '/':
                
# @lc code=end



#
# @lcpr case=start
# "3+2*2"\n
# @lcpr case=end

# @lcpr case=start
# " 3/2 "\n
# @lcpr case=end

# @lcpr case=start
# " 3+5 / 2 "\n
# @lcpr case=end

#


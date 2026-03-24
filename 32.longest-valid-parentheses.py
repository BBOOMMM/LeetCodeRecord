#
# @lc app=leetcode.cn id=32 lang=python3
# @lcpr version=30204
#
# [32] 最长有效括号
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        low = 0
        high = 0
        left_num = 0
        right_num = 0
        max_len = 0
        while high < n and low < n:
            if s[high] == '(':
                left_num += 1
            else:
                right_num += 1
            if left_num == right_num:
                max_len = max(max_len, left_num * 2)
            elif right_num > left_num:
                low = high + 1
                left_num = 0
                right_num = 0
            high += 1
        # 这种无法处理遍历时左括号数量始终大于右括号数量的情况，例如：(()(()，需要反向遍历一次
        left_num = 0
        right_num = 0
        low = n - 1
        high = n - 1
        while high >= 0 and low >= 0:
            if s[high] == '(':
                left_num += 1
            else:
                right_num += 1
            if left_num == right_num:
                max_len = max(max_len, left_num * 2)
            elif left_num > right_num:
                low = high - 1
                left_num = 0
                right_num = 0
            high -= 1
        
        return max_len
# @lc code=end



#
# @lcpr case=start
# "(()"\n
# @lcpr case=end

# @lcpr case=start
# ")()())"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

#


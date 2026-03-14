#
# @lc app=leetcode.cn id=647 lang=python3
# @lcpr version=30204
#
# [647] 回文子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # 奇数回文
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            
            # 偶数回文
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
        return count
# @lc code=end



#
# @lcpr case=start
# "abc"\n
# @lcpr case=end

# @lcpr case=start
# "aaa"\n
# @lcpr case=end

#


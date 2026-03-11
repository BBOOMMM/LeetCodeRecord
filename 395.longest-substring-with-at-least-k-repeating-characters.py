#
# @lc app=leetcode.cn id=395 lang=python3
# @lcpr version=30204
#
# [395] 至少有 K 个重复字符的最长子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def max_length(self, states, min_val, k):
        count = 0
        for i in range(26):
            if states[i] > 0 and states[i] < k:
                count += 1
        return count
    
    
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        left, right = 0, n-1
        states = [0] * 26
        for i in range(n):
            states[ord(s[i]) - ord('a')] += 1
        min_val = min(states)

#
# @lcpr case=start
# "aaabb"\n3\n
# @lcpr case=end

# @lcpr case=start
# "ababbc"\n2\n
# @lcpr case=end

#


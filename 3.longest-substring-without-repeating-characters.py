#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30204
#
# [3] 无重复字符的最长子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_record = set()
        max_len = 0
        p = 0
        for q in range(len(s)):
            word = s[q]
            if word not in set_record:
                set_record.add(word)
                max_len = max(max_len, len(set_record))
            else:
                while word in set_record:
                    set_record.remove(s[p])
                    p += 1
                set_record.add(word)
        return max_len
# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#


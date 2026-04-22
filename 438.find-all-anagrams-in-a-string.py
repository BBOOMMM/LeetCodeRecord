#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30204
#
# [438] 找到字符串中所有字母异位词
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_l = [0] * 128
        s_l = [0] * 128
        for p_char in p:
            p_l[ord(p_char)] += 1
        if len(p) > len(s):
            return []
        re = []
        for i in range(len(p)):
            s_char = s[i]
            s_l[ord(s_char)] += 1
        if s_l == p_l:
            re.append(0)
            
        for i in range(len(p), len(s)):
            remove_char = s[i-len(p)]
            s_l[ord(remove_char)] -= 1
            add_char = s[i]
            s_l[ord(add_char)] += 1
            if s_l == p_l:
                re.append(i-len(p)+1)
        
        return re
            
# @lc code=end



#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#


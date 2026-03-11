#
# @lc app=leetcode.cn id=5 lang=python3
# @lcpr version=30204
#
# [5] 最长回文子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxLenIndex(self, s, n, idx):
        max_len = 1
        start, end = None, None
        
        l1 = idx - 1
        h1 = idx + 1
        while l1>=0 and h1<=n-1 and s[l1]==s[h1]:
            l1 -= 1
            h1 += 1
        max_len = max(max_len, h1-l1-1)
        start = l1 + 1
        end = h1
        
        if idx+1<=n-1 and s[idx]==s[idx+1]:
            l2 = idx - 1
            h2 = idx + 2
            while l2>=0 and h2<=n-1 and s[l2]==s[h2]:
                l2 -= 1
                h2 += 1
            if h2-l2-1 > max_len:
                max_len = h2-l2-1
                start = l2 + 1
                end = h2
        
        return max_len, start, end
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n==0:
            return s
        ans_len = 1
        ans_start = 0
        ans_end = 1
        for idx in range(n):
            max_len, start, end = self.maxLenIndex(s,n,idx)
            if max_len > ans_len:
                ans_len = max_len
                ans_start = start
                ans_end = end
        return s[ans_start : ans_end]
        
# @lc code=end



#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#


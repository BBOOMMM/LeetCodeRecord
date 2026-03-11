#
# @lc app=leetcode.cn id=8 lang=python3
# @lcpr version=30204
#
# [8] 字符串转换整数 (atoi)
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        ans = 0
        while i<n and s[i]==' ':
            i += 1
        
        sign = 1
        if i<n and s[i]=='-':
            sign = -1
            i += 1
        elif i<n and s[i]=='+':
            i += 1
        
        while i<n and s[i]=='0':
            i += 1
        
        while i<n and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            i += 1
        
        boundary = None
        if sign == -1:
            boundary = 1<<31
        else:
            boundary = (1<<31) - 1
        
        if ans > boundary:
            ans = boundary
        
        ans = ans * sign
        return ans
# @lc code=end



#
# @lcpr case=start
# "42"\n
# @lcpr case=end

# @lcpr case=start
# " -042"\n
# @lcpr case=end

# @lcpr case=start
# "1337c0d3"\n
# @lcpr case=end

# @lcpr case=start
# "0-1"\n
# @lcpr case=end

# @lcpr case=start
# "words and 987"\n
# @lcpr case=end

#


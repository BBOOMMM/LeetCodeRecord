#
# @lc app=leetcode.cn id=97 lang=python3
# @lcpr version=30204
#
# [97] 交错字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        i, j = 0, 0
        for k in range(n3):
            if i < n1 and s1[i] == s3[k]:
                i += 1
            elif j < n2 and s2[j] == s3[k]:5
                j += 1
            else:
                return False
        return True
# @lc code=end



#
# @lcpr case=start
# "aabcc"\n"dbbca"\n"aadbbcbcac"\n
# @lcpr case=end

# @lcpr case=start
# "aabcc"\n"dbbca"\n"aadbbbaccc"\n
# @lcpr case=end

# @lcpr case=start
# ""\n""\n""\n
# @lcpr case=end

#


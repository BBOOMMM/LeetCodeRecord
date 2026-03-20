#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30204
#
# [76] 最小覆盖子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len = len(s)
        t_len = len(t)
        
        if t_len > s_len:
            return ""
        
        # 之前每次检查都要比较字符数组，需要字母表长度，这里用diff优化，记录s和t不同字符的数量区别
        diff = {}
        for i in range(t_len):
            diff[t[i]] = diff.get(t[i], 0) - 1
        kinds = len(diff) # 记录不同字符种类数量
        cur_kinds = 0
        
        # max_len = float('inf')
        ans_left = -1
        ans_right = s_len
        low = 0
        quick = 0
        while quick < s_len:
            char = s[quick]
            if char in diff:
                diff[char] += 1
                if diff[char] == 0:
                    cur_kinds += 1
                
            while cur_kinds == kinds:
                # max_len = min(max_len, quick - low + 1)
                if quick - low + 1 < ans_right - ans_left + 1:
                    ans_right = quick
                    ans_left = low
                remove_char = s[low]
                if remove_char in diff:
                    # diff[remove_char] -= 1
                    # if diff[remove_char] == 0:
                    #     cur_kinds -= 1
                    # 这里不对，因为diff[remove_char]可能刚好就是0
                    if diff[remove_char] == 0:
                        cur_kinds -= 1
                    diff[remove_char] -= 1
                low += 1
            
            quick += 1
        
        if ans_left == -1:
            return ""
        return s[ans_left: ans_right+1]
                
            
            
# @lc code=end



#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#


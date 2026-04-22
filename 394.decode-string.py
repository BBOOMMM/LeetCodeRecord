#
# @lc app=leetcode.cn id=394 lang=python3
# @lcpr version=30204
#
# [394] 字符串解码
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def decodeString(self, s: str):
        if s.isalpha():
            return s
        # 一定是有括号
        # 去除首尾字符
        before = ""
        start = 0
        for i in range(len(s)):
            if s[i].isalpha():
                before = before + s[i]
            else:
                start = i
                break
        after = ""
        end = len(s)-1
        for j in range(len(s)-1, -1, -1):
            if s[j].isalpha():
                after = s[j] + after
            else:
                end = j
                break
        
        ans = before
        
        left_num = 0
        right_num = 0
        num = 0
        begin = None
        for i in range(start, end+1):
            if s[i].isdigit() and left_num==right_num:
                num = num*10 + int(s[i])
            else:
                if s[i] == '[':
                    if left_num == right_num:
                        begin = i+1
                    left_num += 1
                elif s[i] == ']':
                    right_num += 1
                    if left_num == right_num:
                        ans = ans + num * self.decodeString(s[begin : i])
                        num = 0
                elif s[i].isalpha(): # 夹在中间的
                    if left_num == right_num:
                        ans = ans + s[i]
        ans += after
        return ans
    
    # def decodeString(self, s: str) -> str:
    #     stack = []
    #     i = 0
    #     n = len(s)
    #     while i < n:
    #         if s[i].isdigit():
    #             num = 0
    #             while i < n and s[i].isdigit():
    #                 num = num * 10 + int(s[i])
    #                 i += 1
    #             stack.append(num)
    #         elif s[i] == '[':
    #             stack.append('[')
    #             i += 1
    #         elif s[i] == ']':
    #             substr = []
    #             while stack and stack[-1] != '[':
    #                 substr.append(stack.pop())
    #             substr.reverse()
    #             stack.pop() # pop '['
    #             repeat_times = stack.pop()
    #             stack.append(''.join(substr) * repeat_times)
    #             i += 1
    #         else:
    #             stack.append(s[i])
    #             i += 1
        
    #     return ''.join(stack)
# @lc code=end



#
# @lcpr case=start
# "3[a]2[bc]"\n
# @lcpr case=end

# @lcpr case=start
# "3[a2[c]]"\n
# @lcpr case=end

# @lcpr case=start
# "2[abc]3[cd]ef"\n
# @lcpr case=end

# @lcpr case=start
# "abc3[cd]xyz"\n
# @lcpr case=end

#


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
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        n = len(s)
        while i < n:
            if s[i].isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                stack.append(num)
            elif s[i] == '[':
                stack.append('[')
                i += 1
            elif s[i] == ']':
                substr = []
                while stack and stack[-1] != '[':
                    substr.append(stack.pop())
                substr.reverse()
                stack.pop() # pop '['
                repeat_times = stack.pop()
                stack.append(''.join(substr) * repeat_times)
                i += 1
            else:
                stack.append(s[i])
                i += 1
        
        return ''.join(stack)
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


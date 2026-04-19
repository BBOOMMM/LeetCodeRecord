# @lcpr-before-debug-begin
from python3problem227 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=227 lang=python3
# @lcpr version=30204
#
# [227] 基本计算器 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def __init__(self):
        self.priority = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
        }
    
    def subcal(self, nums, ops, right=False):
        # 只算一步
        num2 = nums.pop()
        num1 = nums.pop()
        if ops[-1] == '+':
            re = num1 + num2
        elif ops[-1] == '-':
            re = num1 - num2
        elif ops[-1] == '*':
            re = num1 * num2
        elif ops[-1] == '/':
            re = num1 // num2
        ops.pop()
        nums.append(re)
            
            
            
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        ops = []
        nums = [0]  # 补零大法
        i = 0
        n = len(s)
        while i<n:
            if s[i] == ' ':
                i += 1
                continue
            elif s[i] == '(':
                ops.append('(')
                i += 1
            elif s[i] == ')':
                while ops[-1]!='(':
                    self.subcal(nums, ops, right=True)
                ops.pop()
                i += 1
            # 只有当前优先级严格高于操作栈顶优先级时，才直接压栈，否则都要直接计算  比如5*2/3, 一定要先算5*2   5+2-3这种其实无所谓，统一先计算
            elif s[i] in '+-*/':
                # (+/-5 和 3 + -2 的情况
                if i>0 and (s[i-1]=='(' or s[i-1] in '+-'):
                    nums.append(0)
                while ops and ops[-1]!='(' and self.priority[s[i]] <= self.priority[ops[-1]]:
                    self.subcal(nums, ops)
                ops.append(s[i])
                i += 1
            elif s[i].isdigit():
                j = i
                cur_num = 0
                while j<n and s[j].isdigit():
                    cur_num = cur_num * 10 + int(s[j])
                    j += 1
                i = j
                nums.append(cur_num)
        
        while ops:
            self.subcal(nums, ops)
        
        return nums[-1]
                
# @lc code=end



#
# @lcpr case=start
# "3+2*2"\n
# @lcpr case=end

# @lcpr case=start
# " 3/2 "\n
# @lcpr case=end

# @lcpr case=start
# " 3+5 / 2 "\n
# @lcpr case=end

#


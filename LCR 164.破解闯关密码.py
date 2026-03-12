#
# @lc app=leetcode.cn id=LCR 164 lang=python3
# @lcpr version=30204
#
# [LCR 164] 破解闯关密码
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import functools

class Solution:
    def crackPassword(self, password: List[int]) -> str:
        def sort_rule(x, y):
            # 返回正数表示第一个参数 x 应该排在第二个参数 y 后面，返回负数表示第一个参数 x 应该排在第二个参数 y 前面，返回零表示两个参数 x 和 y 的顺序不变。
            a, b = x + y, y + x
            if a > b: return 1
            elif a < b: return -1
            else: return 0
        
        strs = [str(num) for num in password]
        strs.sort(key = functools.cmp_to_key(sort_rule))
        return ''.join(strs)
# @lc code=end



#
# @lcpr case=start
# [15, 8, 7]\n
# @lcpr case=end

# @lcpr case=start
# [0, 3, 30, 34, 5, 9]\n
# @lcpr case=end

#


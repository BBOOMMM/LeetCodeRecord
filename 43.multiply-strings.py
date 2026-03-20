#
# @lc app=leetcode.cn id=43 lang=python3
# @lcpr version=30204
#
# [43] 字符串相乘
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        m = len(num1)
        n = len(num2)
        # 相乘位数最多为 m + n (可以按10的几次方推导证明), 最少为
        # (10^m - 1) * (10^n - 1) = 10^(m+n) - 10^m - 10^n + 1 > 10^(m+n-1)  < 10^(m+n)
        ans = [0] * (m+n)
        
        # 低位到高位是从后往前遍历
        for i in range(m-1, -1, -1):
            x = int(num1[i])
            for j in range(n-1, -1, -1):
                y = int(num2[j])
                # 计算位置位于 i+j+1
                ans[i+j+1] += x*y
        
        # 低位到高位处理进位
        for i in range(m+n-1, 0, -1):
            ans[i-1] += ans[i] // 10
            ans[i] = ans[i] % 10
        
        if ans[0]==0:
            return ''.join([str(x) for x in ans[1:]])
        return ''.join([str(x) for x in ans])
        
# @lc code=end



#
# @lcpr case=start
# "2"\n"3"\n
# @lcpr case=end

# @lcpr case=start
# "123"\n"456"\n
# @lcpr case=end

#


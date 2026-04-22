#
# @lc app=leetcode.cn id=739 lang=python3
# @lcpr version=30204
#
# [739] 每日温度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 搞一个单调栈，保证是递减的
        s = []
        n = len(temperatures)
        re = [0] * n
        for i in range(len(temperatures)):
            if not s:
                s.append(i)
            elif temperatures[i] <= temperatures[s[-1]]:
                s.append(i)
            else: # temperatures[i] > s[-1]
                while s and temperatures[i] > temperatures[s[-1]]:
                    index = s.pop()
                    re[index] = i - index
                s.append(i)
        return re
# @lc code=end



#
# @lcpr case=start
# [73,74,75,71,69,72,76,73]\n
# @lcpr case=end

# @lcpr case=start
# [30,40,50,60]\n
# @lcpr case=end

# @lcpr case=start
# [30,60,90]\n
# @lcpr case=end

#


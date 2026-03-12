#
# @lc app=leetcode.cn id=1288 lang=python3
# @lcpr version=30204
#
# [1288] 删除被覆盖区间
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # start 从小到大排， end 从大到小排
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        n = len(intervals)
        max_end = intervals[0][1]
        
        for i in range(1, n):
            if intervals[i][1] <= max_end:
                count += 1
            else:
                max_end = intervals[i][1]
        
        return n - count
            
        
# @lc code=end



#
# @lcpr case=start
# [[1,4],[3,6],[2,8]]\n
# @lcpr case=end

#


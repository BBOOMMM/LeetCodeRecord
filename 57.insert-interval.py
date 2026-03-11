#
# @lc app=leetcode.cn id=57 lang=python3
# @lcpr version=30204
#
# [57] 插入区间
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        tar_start, tar_end = newInterval
        ans = []
        insert_start, insert_end = tar_start, tar_end
        idx = None
        insert = False
        for i in range(len(intervals)):
            cur_start, cur_end = intervals[i]

            if insert_start > cur_end:
                ans.append([cur_start, cur_end])
            else: # insert_start <= cur_end
                if insert_end >= cur_start:
                    insert_start = min(insert_start, cur_start)
                    insert_end = max(insert_end, cur_end)
                else: # insert_end < cur_start
                    ans.append([insert_start, insert_end])
                    insert = True
                    idx = i
                    break
        if not insert:
            ans.append([insert_start, insert_end])
        if idx is not None:
            ans.extend(intervals[idx:])
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,3],[6,9]]\n[2,5]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,5],[6,7],[8,10],[12,16]]\n[4,8]\n
# @lcpr case=end

#


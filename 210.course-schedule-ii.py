#
# @lc app=leetcode.cn id=210 lang=python3
# @lcpr version=30204
#
# [210] 课程表 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        for prerequisite in prerequisites:
            ai, bi = prerequisite
            indegree[ai] += 1
        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        ans = []
        while len(queue):
            course = queue.popleft()
            ans.append(course)
            for prerequisite in prerequisites:
                ai, bi = prerequisite
                if course==bi:
                    indegree[ai] -= 1
                    if indegree[ai]==0:
                        queue.append(ai)
        if len(ans)==numCourses:
            return ans
        return []
# @lc code=end



#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[1,0],[2,0],[3,1],[3,2]]\n
# @lcpr case=end

# @lcpr case=start
# 1\n[]\n
# @lcpr case=end

#


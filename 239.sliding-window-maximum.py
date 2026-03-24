#
# @lc app=leetcode.cn id=239 lang=python3
# @lcpr version=30204
#
# [239] 滑动窗口最大值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 方法一：用优先队列，存的是元素值和元素索引，优先级为元素值，时间复杂度 O(nlogn)，空间复杂度 O(n)
        import heapq
        n = len(nums)
        if n == 0:
            return []
        q = []
        # python 默认是小顶堆
        for i in range(k):
            heapq.heappush(q, (-nums[i], i))
        res = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            res.append(-q[0][0])
        return res

        # 方法二：单调队列，存的是元素索引
        from collections import deque
        n = len(nums)
        if n == 0:
            return []
        q = deque()
        res = []
        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        for i in range(k, n):
            while q and q[0] <= i - k:
                q.popleft()
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            res.append(nums[q[0]])
        return res

# @lc code=end



#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=528 lang=python3
# @lcpr version=30204
#
# [528] 按权重随机选择
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import random

class Solution:
    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.presum = []
        cur_sum = 0
        for i in range(len(w)):
            cur_sum += w[i]
            self.presum.append(cur_sum)

    def pickIndex(self) -> int:
        x = random.randint(1, self.total)
        # [ presum[i]-w[i]+1 , presum[i] ]
        # [ presum[i-1]+1 , presum[i] ]
        # 找到使得 x 满足这个区间的 i
        left = 0
        right = len(self.presum)-1
        while left <= right:
            mid = (left+right)//2
            if (x<=self.presum[mid] and mid==0) or (x<=self.presum[mid] and x>=self.presum[mid-1]+1):
                return mid
            elif x > self.presum[mid]:
                left = mid + 1
            else:
                right = mid - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end



#
# @lcpr case=start
# ["Solution","pickIndex"][[[1]],[]]\n
# @lcpr case=end

# @lcpr case=start
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"][[[1,3]],[],[],[],[],[]]\n
# @lcpr case=end

#


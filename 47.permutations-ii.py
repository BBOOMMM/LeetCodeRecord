#
# @lc app=leetcode.cn id=47 lang=python3
# @lcpr version=30204
#
# [47] 全排列 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def __init__(self):
        self.ans = []
        self.path = []

    def traverse(self, nums, used):
        if len(self.path) == len(nums):
            self.ans.append(self.path[:])
            return

        for i in range(len(nums)):
            # 这是处理同一层的
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            # 这是处理纵向的
            if used[i]:
                continue
            self.path.append(nums[i])
            used[i] = True
            self.traverse(nums, used)
            self.path.pop()
            used[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 同层一样的就是重复
        nums.sort()
        n = len(nums)
        used = [False] * n
        self.traverse(nums, used)
        return self.ans
# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=16 lang=python3
# @lcpr version=30204
#
# [16] 最接近的三数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = float('inf')

        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, n-1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if abs(sum_ - target) < abs(ans - target):
                    ans = sum_

                if sum_ < target:
                    left += 1
                elif sum_ > target:
                    right -= 1
                else:
                    return target
        
        return ans
# @lc code=end



#
# @lcpr case=start
# [-1,2,1,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n1\n
# @lcpr case=end

#


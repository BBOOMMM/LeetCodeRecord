#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30204
#
# [42] 接雨水
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 每个点能存储的水，取决于左边最大值和右边最大值的较小者
        vol = 0
        leftmax = 0
        rightmax = 0
        left = 0
        right = len(height) - 1
        while left <= right:
            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])
            
            if leftmax <= rightmax:
                vol += (leftmax - height[left])
                left += 1
            else:
                vol += (rightmax - height[right])
                right -= 1
        return vol
# @lc code=end



#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#


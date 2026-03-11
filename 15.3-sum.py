#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30204
#
# [15] 三数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num1 = nums[i]
            
            target = -num1
            j = i + 1
            k = n - 1
            while j < k:
                cur = nums[j] + nums[k]
                if cur == target:
                    res.append([num1, nums[j], nums[k]])
                    j += 1
                    # 需要添加 while 边界判断
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                elif cur < target:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                else:
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
        return res
# @lc code=end



#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#


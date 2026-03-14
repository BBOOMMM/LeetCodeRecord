#
# @lc app=leetcode.cn id=611 lang=python3
# @lcpr version=30204
#
# [611] 有效三角形的个数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        
        # for i in range(0, n-2):
        #     j = i + 1
        #     k = n - 1
        #     while j < k:
        #         if nums[i] + nums[j] > nums[k]:
        #             # 后面更大的 nums[j] 一定都可以
        #             count += (k - j)
        #             k -= 1
        #         else:
        #             pass
        #             # 也可以 k -= 1
        #             # j += 1 or k -= 1 ?
        #             # 正向会出问题
                    
        for i in range(n-1, 1, -1):
            j = 0
            k = i - 1
            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    # 后面更大的 nums[j] 一定都可以
                    count += (k - j)
                    k -= 1
                else:
                    j += 1
        
        return count
# @lc code=end



#
# @lcpr case=start
# [2,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,3,4]\n
# @lcpr case=end

#


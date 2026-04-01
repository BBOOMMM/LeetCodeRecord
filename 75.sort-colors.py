#
# @lc app=leetcode.cn id=75 lang=python3
# @lcpr version=30204
#
# [75] 颜色分类
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # p0, p1都是下一个位置，情况更少更简单
        n = len(nums)
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1
        return nums
        
        # p0 0结束末尾，p1 1结束末尾
        p0 = -1
        p1 = -1
        for i in range(len(nums)):
            cur_num = nums[i]
            if cur_num == 0:
                if p1<=p0:  # 还没有 1
                    tmp = nums[p0+1]
                    p0 += 1
                    nums[p0] = 0
                    p1 = p0
                    nums[i] = tmp
                else:
                    p0 += 1
                    nums[p0] = 0
                    tmp = nums[p1+1]
                    p1 += 1
                    nums[p1] = 1
                    if p1 < i:
                        nums[i] = tmp
            elif cur_num == 1:
                tmp = nums[p1+1]
                p1 += 1
                nums[p1] = 1
                nums[i] = tmp
            else: # 2
                continue
            
        return nums
# @lc code=end



#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#


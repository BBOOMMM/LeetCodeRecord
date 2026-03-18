#
# @lc app=leetcode.cn id=523 lang=python3
# @lcpr version=30204
#
# [523] 连续的子数组和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 前缀和 + 哈希表
        # 前缀和 mod k 的结果相同，说明中间的部分是 k 的倍数
        prefix_sum = 0
        mod_map = {0: -1}
        for i in range(len(nums)):
            prefix_sum += nums[i]
            cur_mod = prefix_sum % k
            if cur_mod in mod_map:
                if i - mod_map[cur_mod] > 1: # 大于1，因为相减算的子数组和实际上是 [mod_map[cur_mod]+1, i]
                    return True
            else:
                mod_map[cur_mod] = i # 只记录第一次出现的位置，因为要保证子数组长度至少为2
        return False
# @lc code=end



#
# @lcpr case=start
# [23,2,4,6,7]\n6\n
# @lcpr case=end

# @lcpr case=start
# [23,2,6,4,7]\n6\n
# @lcpr case=end

# @lcpr case=start
# [23,2,6,4,7]\n13\n
# @lcpr case=end

#


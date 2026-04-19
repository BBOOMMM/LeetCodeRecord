#
# @lc app=leetcode.cn id=108 lang=python3
# @lcpr version=30204
#
# [108] 将有序数组转换为二叉搜索树
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, nums, left, right):
        # 找中间放两边
        if left > right:
            return None
        
        mid = (left + right) // 2
        val = nums[mid]
        node = TreeNode(val)
        node.left = self.buildTree(nums, left, mid-1)
        node.right = self.buildTree(nums, mid+1, right)
        
        return node
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildTree(nums, 0, len(nums)-1)
# @lc code=end



#
# @lcpr case=start
# [-10,-3,0,5,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,3]\n
# @lcpr case=end

#


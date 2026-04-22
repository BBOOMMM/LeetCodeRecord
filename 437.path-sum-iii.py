#
# @lc app=leetcode.cn id=437 lang=python3
# @lcpr version=30204
#
# [437] 路径总和 III
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
    def __init__(self):
        self.presum_dict = {0:1}
        self.ans = 0
        self.presum = 0
    
    # 先序遍历
    def preorder(self, root, target):
        if not root:
            return
        
        self.presum += root.val
        self.ans += self.presum_dict.get(self.presum-target, 0)
        self.presum_dict[self.presum] = self.presum_dict.get(self.presum, 0) + 1
        
        self.preorder(root.left, target)
        self.preorder(root.right, target)
        
        self.presum_dict[self.presum] -= 1
        self.presum -= root.val
        
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.preorder(root, targetSum)
        return self.ans
# @lc code=end



#
# @lcpr case=start
# [10,5,-3,3,2,null,11,3,-2,null,1]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
# @lcpr case=end

#


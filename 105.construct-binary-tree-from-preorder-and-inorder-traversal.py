#
# @lc app=leetcode.cn id=105 lang=python3
# @lcpr version=30204
#
# [105] 从前序与中序遍历序列构造二叉树
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
    def build(self, preorder, inorder, pre_left, pre_right, in_left, in_right):
        if pre_left > pre_right or in_left > in_right:
            return
        val = preorder[pre_left]
        new_node = TreeNode(val)
        idx = None
        for i in range(in_left, in_right+1):
            if inorder[i] == val:
                idx = i
                break
        length = idx - in_left
        new_node.left = self.build(preorder, inorder, pre_left+1, pre_left+length, in_left, idx-1)
        new_node.right = self.build(preorder, inorder, pre_left+length+1, pre_right, idx+1, in_right)
        return new_node
    
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 前序第一个一定是根节点，中序对应前面就是左子树
        return self.build(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)
        
        
        
# @lc code=end



#
# @lcpr case=start
# [3,9,20,15,7]\n[9,3,15,20,7]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#


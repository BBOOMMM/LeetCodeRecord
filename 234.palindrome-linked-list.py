#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=30204
#
# [234] 回文链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def ReverseListNode(self, head):
        pre = None
        p = head
        while p:
            tmp = p.next 
            p.next = pre 
            pre = p 
            p = tmp 
        # pre 变成头节点
        return pre 
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 思路：找到中间节点，把这个节点之后反转，比较，再反转恢复
        p, q = head, head
        # p.next 是要开始反转的位置
        while q.next and q.next.next:
            p = p.next 
            q = q.next.next 
        to_connect = p
        reverse_node = p.next 
        p.next = None
        
        reverse_head = self.ReverseListNode(reverse_node)
        q = reverse_head
        p = head
        while p and q:
            if p.val != q.val:
                return False
            p = p.next 
            q = q.next 
        _ = self.ReverseListNode(reverse_head)
        to_connect.next = reverse_node
        
        return True
        
        
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#


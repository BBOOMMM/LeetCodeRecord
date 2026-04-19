#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30204
#
# [2] 两数相加
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        dummy = ListNode()
        jinwei = 0
        p = dummy
        while p1 and p2:
            val = p1.val + p2.val + jinwei
            new_node = ListNode(val%10)
            jinwei = val // 10
            p.next = new_node
            p = new_node
            p1 = p1.next 
            p2 = p2.next 
        if p1 or p2:
            p3 = p1 if p1 else p2 
            while p3:
                val = p3.val + jinwei
                new_node = ListNode(val%10)
                jinwei = val // 10
                p.next = new_node
                p = new_node
                p3 = p3.next 
        if jinwei:
            new_node = ListNode(jinwei)
            p.next = new_node
            p = new_node
        return dummy.next
        
# @lc code=end



#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#


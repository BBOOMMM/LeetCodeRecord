#
# @lc app=leetcode.cn id=21 lang=python3
# @lcpr version=30204
#
# [21] 合并两个有序链表
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = list1, list2
        dummy = ListNode()
        cur = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                cur = head1
                head1 = head1.next
            else:
                cur.next = head2
                cur = head2
                head2 = head2.next
        if head1:
            cur.next = head1
        elif head2:
            cur.next = head2
        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#


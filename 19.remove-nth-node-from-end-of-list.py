#
# @lc app=leetcode.cn id=19 lang=python3
# @lcpr version=30204
#
# [19] 删除链表的倒数第 N 个结点
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 双指针，dummy-head
        # 想让慢指针指向倒数第 n+1 个节点，这样才好删除
        # 快指针先跑 n
        # 当快指针指向最后一个节点的时候，慢指针指向倒数第 n+1 个节点
        dummy = ListNode(0, next=head)
        low = dummy
        quick = dummy
        k = n
        while k:
            quick = quick.next
            k-=1
        while quick.next:
            quick = quick.next 
            low = low.next 
        to_remove = low.next 
        next_node = low.next.next 
        # del 变量 ≠ 删除对象，仅删除引用标签
        # del to_remove 无用
        low.next = next_node
        # 面对只有一个节点的情况，必须return dummy.next 而不是 head
        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=4 lang=python3
# @lcpr version=30204
#
# [4] 寻找两个正序数组的中位数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        k = ((m + n) // 2) + 1
        # 如果 m + n 是奇数, 就是从小到大第 k 个数
        if (m+n) % 2==0:
            k -= 1
        # 如果 m + n 是偶数, 就是从小到大第 k 个数和第 k+1 个数的均值
        left1 = 0
        left2 = 0
        while k >= 2:
            idx = k // 2
            if left1 >= m:
                left2 += idx
                k -= idx 
                continue
            elif left2 >= n:
                left1 += idx
                k -= idx 
                continue

            if left1+idx-1 >= m:
                idx = m - left1 
            if left2+idx-1 >= n:
                idx = n - left2
            if nums1[left1+idx-1] > nums2[left2+idx-1]:
                left2 += idx
            else:
                left1 += idx
            k -= idx 
        # k = 1  第一大
        if (m+n)%2 == 1:
            if left1 >= m:
                return nums2[left2]
            elif left2 >= n:
                return nums1[left1]
            return min(nums1[left1], nums2[left2])
        else:
            # 第 k 大
            if left1 >= m:
                return (nums2[left2]+nums2[left2+1])/2.0
            elif left2 >= n:
                return (nums1[left1]+nums1[left1+1])/2.0
            
            if nums1[left1] > nums2[left2]:
                k_max = nums2[left2]
                left2 += 1
            elif nums1[left1] < nums2[left2]:
                k_max = nums1[left1]
                left1 += 1
            else:
                return nums1[left1]
            if left1 >= m:
                k1_max = nums2[left2]
            elif left2 >= n:
                k1_max = nums1[left1]
            else:
                k1_max = min(nums1[left1], nums2[left2])
            return (k_max + k1_max)/2.0
# @lc code=end



#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=347 lang=python3
# @lcpr version=30204
#
# [347] 前 K 个高频元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import random

class Solution:
    def __init__(self):
        self.ans = []
    
    def quickSort(self, frequency, low, high, k):
        if low > high:
            return
        elif low == high:
            assert k == 1
            self.ans.append(frequency[low][1])
            return 
        idx = random.randint(low, high)
        frequency[high], frequency[idx] = frequency[idx], frequency[high]
        pivot = frequency[high][0]
        # 从大到小排序
        i = low - 1
        j = high
        while i<j:
            i+=1
            while frequency[i][0] > pivot and i<j:
                i+=1
            j-=1
            while frequency[j][0] < pivot and i<j:
                j-=1
            if i<j:
                frequency[i], frequency[j] = frequency[j], frequency[i]
        frequency[i], frequency[high] = frequency[high], frequency[i]
        # [low, i-1] >= pivot
        # i == pivot
        # [i, high] <= pivot
        if k <= i-low+1: 
            self.quickSort(frequency, low, i, k)
        else:
            for m in range(low, i+1):
                self.ans.append(frequency[m][1])
            self.quickSort(frequency, i+1, high, k-(i-low+1))
            
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        frequency = []
        for key in d:
            frequency.append([d[key], key])
        # print(frequency)
        
        self.quickSort(frequency, 0, len(frequency)-1, k)
        return self.ans
# @lc code=end



#
# @lcpr case=start
# [1,1,1,2,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,2,1,2,3,1,3,2]\n2\n
# @lcpr case=end

#


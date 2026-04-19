#
# @lc app=leetcode.cn id=295 lang=python3
# @lcpr version=30204
#
# [295] 数据流的中位数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq

class MedianFinder:

    def __init__(self):
        # 对顶堆，左边是大顶堆（存小元素，堆顶是小元素中最大的），右边是小顶堆（存大元素，堆顶是大元素中最小的）
        # python 默认小顶堆
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap)==0:
            heapq.heappush(self.max_heap, -num)
            return 
        max_max_heap = -self.max_heap[0]
        if num > max_max_heap:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        # 两者平衡
        if len(self.max_heap) > len(self.min_heap)+1:
            tmp = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, tmp)
        elif len(self.min_heap) > len(self.max_heap):
            tmp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -tmp)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end




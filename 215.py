import heapq
class Solution:
    def findKthLargest(self, nums, k) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:] :
            #print("heap:",heap)
            if heap[0] < num :
                    heapq.heappushpop(heap,num)
        return heapq.heappop(heap)
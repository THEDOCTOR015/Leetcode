"""
Answer (no fun) :
"""
import heapq
class MedianFinder:

    def __init__(self):
        self.minheap = [] # Contient les grand nombres
        self.maxheap = [] # Attention a inverser les valeurs (Contient les petis nombres)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)
        heapq.heappush(self.minheap, -self.maxheap[0])
        heapq.heappop(self.maxheap)
        # On realimente la maxheap si besoin
        if len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap, -self.minheap[0])
            heapq.heappop(self.minheap)

    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap) :
            return (self.maxheap[0] + self.minheap[0])/2.0
        return self.maxheap[0]
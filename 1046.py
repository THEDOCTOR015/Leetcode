import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones ]
        heapq.heapify(stones)
        while len(stones) > 1 :
            res = heapq.heappop(stones) - heapq.heappop(stones)
            heapq.heappush(stones,res)
        if len(stones) == 1 :
            return -(stones[0])
        return 0
        
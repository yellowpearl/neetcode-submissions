import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            l = heapq.heappop_max(stones)
            r = heapq.heappop_max(stones)
            if l > r:
                heapq.heappush_max(stones, l-r)
        return stones[0] if len(stones) > 0 else 0

import heapq

from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            from_, to = edges[i]
            succ = succProb[i]
            adj[from_].append((succ, to))
            adj[to].append((succ, from_))

        h = [(1, start_node)]
        success = {}
        while h and end_node not in success:

            succ, node = heapq.heappop_max(h)
            if node in success:
                continue
            
            success[node] = succ
            for s_n, n in adj[node]:
                heapq.heappush_max(h, (s_n*succ, n))
        return success[end_node] if end_node in success else 0.0

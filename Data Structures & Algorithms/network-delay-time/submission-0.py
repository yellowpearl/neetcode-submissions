import heapq

from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for ui, vi, ti in times:
            adj[ui].append((vi, ti))
        
        h = [(0, k)]
        shortest = {}
        while h:
            val, node = heapq.heappop(h)
            if node in shortest:
                continue
            shortest[node] = val

            for dest_node, dest_val in adj[node]:
                if dest_node not in shortest:
                    heapq.heappush(h, (dest_val+val, dest_node))
        
        if len(shortest) != n:
            return -1
        return max(shortest.values())


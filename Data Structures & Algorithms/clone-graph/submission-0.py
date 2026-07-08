"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visit = set()
        nodes = {}
        q = deque()
        visit.add(node.val)
        q.append(node)

        while q:
            for i in range(len(q)):
                n = q.popleft()

                if n.val not in nodes:
                    nodes[n.val] = []
                for neighbor in n.neighbors:
                    nodes[n.val].append(neighbor.val)

                    if neighbor.val not in visit:
                        q.append(neighbor)
                        visit.add(neighbor.val)
        
        nodes_by_val = {}
        for key in nodes.keys():
            nodes_by_val[key] = Node(val=key)
        
        for key, values in nodes.items():
            for v in values:
                nodes_by_val[key].neighbors.append(nodes_by_val[v])
            
        for k, v in nodes_by_val.items():
            return v











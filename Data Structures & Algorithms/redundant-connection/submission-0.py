class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        e_s = set()
        par = {}
        rank = {}

        for f, t in edges:
            e_s.add(f)
            e_s.add(t)
        
        for edge in e_s:
            par[edge] = edge
            rank[edge] = 0
        
        def find(e: int) -> int:
            p = par[e]
            
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(e1, e2):
            p1, p2 = find(e1), find(e2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p1] > rank[p2]:
                par[p1] = p2
            else:
                par[p1] = p2
                rank[p2] += 1
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]









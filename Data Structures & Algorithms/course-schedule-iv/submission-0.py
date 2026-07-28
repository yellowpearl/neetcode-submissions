from collections import defaultdict
from copy import copy
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = defaultdict(list)
        for f, t in prerequisites:
            adj[t].append(f)
        
        available_orig = set()
        for i in range(numCourses):
            available_orig.add(i)
        
        def dfs(v, orig, visit, available, mem):
            if v in visit:
                return
            
            visit.add(v)

            for n in adj[v]:
                mem[orig].add(n)
                dfs(n, orig, visit, available, mem)
            
            available.add(v)
        
        res = {}
        mem = {}
        for i in range(numCourses):
            a = available_orig.copy()
            visit = set()
            mem[i] = set()
            dfs(i, i, visit, a, mem)
            res[i] = a
        
        r = []
        for uj, vj in queries:
            r.append(uj in mem[vj])
        return r



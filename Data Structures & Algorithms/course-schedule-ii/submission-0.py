from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        available = set()
        for f, t in prerequisites:
            adj[t].append(f)
        for i in range(numCourses):
            if i not in adj:
                available.add(i)
        
        visit = set()
        path = set()
        res = []
        def dfs(v, visit, path, available, res):
            if v in path:
                return False
            if v in visit:
                return True
            
            visit.add(v)
            path.add(v)

            for n in adj[v]:
                r = dfs(n, visit, path, available, res)
                if not r:
                    return False
            
            available.add(v)
            res.append(v)
            path.remove(v)
            return True
        
        for i in range(numCourses):
            r = dfs(i, visit, path, available, res)
            if not r:
                return []
        res.reverse()
        return res

            

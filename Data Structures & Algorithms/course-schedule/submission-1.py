from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for f, t in prerequisites:
            adj[t].append(f)

        available = set()
        for i in range(1, numCourses+1):
            if i not in adj:
                available.add(i)


        visit = set()
        path = set()
        def dfs(v, visit, path, available):
            if v in path:
                return False
            if v in visit:
                return True
            
            visit.add(v)
            path.add(v)


            for node in adj[v]:
                r = dfs(node, visit, path, available)
                if not r:
                    return False
            
            available.add(v)
            path.remove(v)
            return True
        
        for i in range(1, numCourses+1):
            r = dfs(i, visit, path, available)
            if not r:
                return False
        return True
            

        






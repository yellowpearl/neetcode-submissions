from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 2 - [[0,1][1]]
        # 3 - [[2,1][1,0]] 
        # 3 - [[2,1][0,1][2,1]] - 
        
        blocked = {}
        for p in prerequisites:
            if p[0] not in blocked:
                blocked[p[0]] = set([p[1]])
            else:
                blocked[p[0]].add(p[1])
        
        free = set()
        for i in range(numCourses):
            if i not in blocked:
                free.add(i)
        
        while len(free) != numCourses:
            f_c = len(free)
            for k, v in blocked.items():
                v_c = v.copy()
                for c in v_c:
                    if c in free:
                        v.remove(c)
                if len(v) == 0:
                    free.add(k)


            f_c_c = len(free)
            if f_c == f_c_c:
                return False

        return True






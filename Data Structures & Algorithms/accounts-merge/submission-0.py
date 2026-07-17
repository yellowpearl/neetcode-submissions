from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        par = {}
        rank = {}

        for idx, acc in enumerate(accounts):
            name = acc[0]
            mails = acc[1:]
            for m in mails:
                par[m] = m
                rank[m] = 1


        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else:
                par[p2] = p1
                rank[p1] += 1
            return True
        
        res = []
        d = defaultdict(set)
        for idx, acc in enumerate(accounts):
            name = acc[0]
            mails = acc[1:]
            m0 = mails[0]
            for m in mails:
                union(m0, m)

        for idx, acc in enumerate(accounts):
            name = acc[0]
            mails = acc[1:]
            m0 = mails[0]
            for m in mails:
                d[(name, find(m))].add(m)   

        for k, v in d.items():
            name, _ = k
            res.append([name, *list(sorted(v))])
        return res
        

            


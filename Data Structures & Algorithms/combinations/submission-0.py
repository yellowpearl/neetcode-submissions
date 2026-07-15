class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def back(i, curr, res):
            if len(curr) == k:
                res.append(curr.copy())
                return
            if i > n:
                return
            
            curr.append(i)
            back(i+1, curr, res)
            curr.pop()
            back(i+1, curr, res)
        
        res = []
        back(1, [], res)
        return res
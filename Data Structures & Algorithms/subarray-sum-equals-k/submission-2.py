from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        seen = {0: 1}
        p = 0
        res = 0
        for n in nums:
            p += n
            res += seen.get(p-k,0)
            seen[p] = seen.get(p, 0) + 1
        return res
        


from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        pref_map = defaultdict(int)
        pref_map[0] += 1
        total = 0
        res = 0

        # -1 -2 -1
        # {0: 1, -1: 2, -2: 1}

        for n in nums:
            total += n
            res += pref_map[total - k]
            pref_map[total] += 1
        return res
        


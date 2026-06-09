from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        res = 0
        for n in nums:
            if not count[n-1]:
                c = 1
                cur_n = n
                while True:
                    res = max(res, c)
                    if count[cur_n+1]:
                        c += 1
                        cur_n += 1
                    else:
                        break
        return res

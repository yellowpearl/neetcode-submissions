from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] += 1
        for c, v in count.items():
            freq[v].append(c)

        res = []
        for f in freq[::-1]:
            for n in f:
                res.append(n)
                if len(res) == k:
                    return res
        

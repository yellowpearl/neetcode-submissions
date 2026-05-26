from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        # [1,2,2,3,3,3] 2
        # {1: 1, 2: 2, 3: 3}
        # (1, 1), (2, 2), (3, 3)
        

        return list([k_v[0] for k_v in sorted(
            count.items(),
            key=lambda k_v: k_v[1],
        )])[-k:]
        

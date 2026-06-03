class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        m = max(people)
        count = [0] * m
        for p in people:
            count[p-1] += 1
        
        l = 0
        r = len(count) - 1
        # 2
        # [5] 0 0
        # [3] 0 0
        # [1] 0 0
        while l <= r:
            if count[l] < 1:
                l += 1
            elif count[r] < 1:
                r -= 1
            else:
                if limit - (r+1) >= l+1:
                    count[r] -= 1
                    count[l] -= 1
                    res += 1
                else:
                    count[r] -= 1
                    res += 1
        return res
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min=1 max=max(piles) 
        # 
        l = 1
        r = max(piles)

        # 1 4 3 2 h=9
        # l=1 r=4 mid=2 hours=6 
        # l=1 r=1
        
        # 25 10 23 4 h=4
        ans = 1
        while l <= r:
            mid = (l + r) // 2

            hours = 0
            for p in piles:
                hours += p // mid
                if p % mid > 0:
                    hours += 1
            
            if hours <= h:
                r = mid - 1
                ans = mid
            elif hours > h:
                l = mid + 1
        return ans

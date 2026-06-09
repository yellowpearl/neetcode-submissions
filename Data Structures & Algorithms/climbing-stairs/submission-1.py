cache = {}

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 1:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        if n not in cache:
            ans = self.climbStairs(n-1)+self.climbStairs(n-2)
            cache[n] = ans
        return cache[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        c = [1, 2]
        i = 2
        while i < n:
            tmp = c[0]
            c[0] = c[1]
            c[1] = c[0] + tmp
            i += 1

        # 4 - [3, 5]
        return c[1]
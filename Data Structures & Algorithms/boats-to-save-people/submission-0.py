class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        res = 0
        # 1, 2, 2, 3
        while l <= r:
            if people[l] <= limit - people[r]:
                l += 1
                r -= 1
                res += 1
            else:
                r -= 1
                res += 1
        return res
